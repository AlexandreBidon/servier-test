# Traitement ad-hoc (bonus)

## Extraire le nom du journal qui mentionne le plus de médicaments différents

Pour répondre à cette question, j'ai réalisé un traitement présent dans `src/processing_ad_hoc/get_journal_most_mention.py`. Ce traitement parcours le JSON et cherche le journal avec le plus de `ref` différentes.

On obtient le résultat suivant :

| Journal | Number of mention |
|---|---|
| Journal of emergency nursing | 2 |
| Psychopharmacology | 2 |
| The journal of maternal-fetal & neonatal medicine | 2 |
| Hôpitaux Universitaires de Genève | 1 |
| American journal of veterinary research | 1 |
| The Journal of pediatrics | 1 |
| Journal of food protection | 1 |
| The journal of allergy and clinical immunology....| 1 |
| Journal of back and musculoskeletal rehabilitation | 1 |
| Journal of photochemistry and photobiology. B, ...  |  1 |
