# Test technique DE Servier

> **Auteur:** Alexandre Bidon
> Data Engineer @ LittleBigCode

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

Ce format convient pour l'exercice. Il serait possible de l'améliorer pour le rendre plus robuste. On pourrait remplacer la catégorie "name" des nodes par un id pour s'assurer de l'unicité des identifiants des nodes.

## Partie 2: SQL

### Première requête

Cette première requête SQL doit permettre de trouver le chiffre d’affaires jour par jour, du 1er janvier 2019 au 31 décembre 2019.

On travaille sur la table *TRANSACTION* qui contient toutes les ventes et leur montant.

```sql
SELECT date,
       SUM(prod_price * prod_qty) AS  ventes 
FROM TRANSACTION 
WHERE date>="01/01/19" and date<="31/12/19" 
GROUP BY date;
```

On multiplie les colonnes *prod_price* et *prod_qty* pour obtenir le montant total d'une commande. On additionne ensuite le résultat pour obtenir le chiffre d'affaires total (**SUM**) d'une journée (**GROUP BY**). On cadre la requête sur la période du 1er janvier 2019 au 31 décembre 2019 à l'aide du **WHERE date>="01/01/19" and date<="31/12/19"**.

## Deuxième requête

Cette deuxième requête doit permettre de déterminer, par client et sur la période allant du 1er janvier 2019 au 31 décembre 2019, les ventes meuble et déco réalisées.

```sql
SELECT client_id, 
       SUM(CASE WHEN product_type = 'MEUBLE' THEN prod_price * prod_qty ELSE 0 END) AS ventes_meuble,
       SUM(CASE WHEN product_type = 'DECO' THEN prod_price * prod_qty ELSE 0 END) AS ventes_deco
FROM TRANSACTION
INNER JOIN PRODUCT_NOMENCLATURE ON TRANSACTION.prod_id = PRODUCT_NOMENCLATURE.product_id
WHERE date>="01/01/19" and date<="31/12/19" 
GROUP BY client_id;
```

On utilise des sommes avec conditions (**CASE**) pour séparer les montants déco et meuble. On réalise une jointure sur les deux tables pour obtenir toutes les informations nécessaires sur les commandes. On regroupe enfin par les montants par client (client_id).