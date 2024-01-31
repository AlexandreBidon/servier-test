# Test technique DE Servier

**Auteur: Alexandre Bidon**

## Partie 1: Python et Data Engineering

### Format du résultat JSON

Pour le fichier de sortie JSON, j'ai décidé d'utiliser le format suivant:

```JSON
{
    "name": "graphe médicament servier",
    "nodes": [
        {
            // Le type de la node
            // journal | pubmed | drug | clinical_trial
            "type": "", 
            // Le nom de la node, dépend du type de la node
            // Le titre du journal | Le nom de la publication | Le nom du médicament | Le nom de l'essai clinique
            "name": ""
        }
    ],
    "links": [
        {
            "from": "",
            "to": "",
            // La date de la mention
            "date": ""
        }
    ]
}
```

## Partie 2: SQL

### Première requête

Cette première requête SQL doit permettre de trouver le chiffre d’affaires jour par jour, du 1er janvier 2019 au 31 décembre 2019.

On travaille sur la table *TRANSACTION* qui contient toutes les ventes et leur montant.

```sql
SELECT SUM(prod_price * prod_qty) AS  total_sales FROM TRANSACTION WHERE date>="01/01/19" and date<="31/12/19" GROUP BY date;
```

On multiplie les colonnes *prod_price* et *prod_qty* pour obtenir le montant total d'une commande. On additionne ensuite le résultat pour obtenir le chiffre d'affaires total (**SUM**) d'une journée (**GROUP BY**). On cadre la requête sur la période du 1er janvier 2019 au 31 décembre 2019 à l'aide du **WHERE date>="01/01/19" and date<="31/12/19"**.

## Deuxième requête


