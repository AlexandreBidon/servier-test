# Choix techniques

[Retour au menu](./00_menu.md)

- [Choix techniques](#choix-techniques)
  - [Stockage des données](#stockage-des-données)
  - [Implémentation de la pipeline python](#implémentation-de-la-pipeline-python)
    - [Structure du projet](#structure-du-projet)
  - [Importation des données](#importation-des-données)
  - [Nettoyage des données](#nettoyage-des-données)

## Stockage des données

Les données du projet sont enregistrées dans un dossier avec l'organisation suivante:

```
📂 data
┣ 📂 01_raw
┣ 📂 02_intermediate
┗ 📂 03_result
```

Le dossier *01_raw* contient les données brutes telles qu'on les recoit. Dans le cadre d'un projet en production, cela correspondrait à un **data lake**.

Le dossier *02_intermediate* contient les résultats intermédiaires. On peut par exemple exporter certaines tables ayant reçu un premier traitement.

Enfin le dossier *03_result* contient la donnée entièrement préparée telle qu'elle est demandée dans l'énoncé.

## Implémentation de la pipeline python

Afin de coder le pipeline de traitement de données en python, il faut sélectionner un framework adapté pour la manipulation de données. Plusieurs choix sont possibles en Python. J'ai opté pour la librairie **pandas**. Cette librairie permet d'importer et de manipuler des dataframes. Ce choix est adapté à la taille des jeux de données. Cependant, ce choix serait moins pertinent avec une mise en production sur des jeux de données plus volumineux. Il serait préferable dans ce cas de figure de choisir un framework comme **Spark**.

### Structure du projet

Le projet est structuré de la manière suivante:

```
📦 package
┣ 📂 data
┃ ┗ 📂 load
┃ ┗ 📂 transform
┗ 📂 processing
```

Le projet a été pensé de manière à répondre à plusieurs besoins:

- Le projet est packagé pour être utilisé facilement
- Le package est découpé en sous module pouvant être utilisé indépendament. Cela permet de réutiliser les modules pour d'autres traitements. Il est aussi possible de controler ces modules dans un pipeline à l'aide d'un outil comme Airflow.

> [!NOTE]
> Dans mon projet, j'ai utilisé la feature *pipe* de **pandas** pour construire ma pipeline.


> [!NOTE]  
> Le module "data/transform" a été testé à l'aide du framework .

## Importation des données

Le module d'importation des données doit répondre à plusieurs besoins:

- Il doit supporter plusieurs types de données en entrée: CSV et JSON
- Il doit s'assurer de l'intégrité des données en entrée (virgule en trop dans le JSON par exemple)
- Il doit retourner toutes les données sous forme de dataframes

## Nettoyage des données

Avant de pouvoir travailler sur les données afin de construire le JSON de sortie, on doit s'assurer que les données soient propres. Pour cela, j'ai identifié les points suivants:

- Certains string présentent des artefacts du au format UTF-8. Il faudrait nettoyer les chaines de caractères pour les retirer.
- Les données présentes des valeurs manquantes, il faudrait idéalement inférer les valeurs manquantes (id) ou les remplacer par des NA

Lorsque les données seront propres, une dernière étape du nettoyage pourra consister à proprement typer les colonnes.
