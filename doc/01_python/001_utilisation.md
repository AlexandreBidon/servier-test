# Comment utiliser le projet

[Retour au menu](./00_menu.md)

## Initialisation de python et des dépendances

Ce projet a été réalisé avec **Python version 3.11.7**. Pour commencer, vous pouvez instancié un environnement virtuel avec les commandes suivantes:

- `python -m venv venv  `
- `.\venv\Scripts\activate`

Vous pouvez ensuite installer les dépendances avec la commande suivante:

- `pip install -r requirements.txt`

## Utilisation du projet

Pour utiliser le projet, il faut appeler le script suivant:

- `python src/main.py`

Par défaut, le script va traiter les données d'entrées et générer le JSON de sortie. Il est possible de choisir un autre traitement à l'aide de l'argument `--pipeline`. On peut par exemple répondre à la première question ad-hoc avec la commande suivante:

- `python src/main.py --pipeline get_mentions`
