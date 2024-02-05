# Pour aller plus loin

[Retour au menu](./00_menu.md)

Je vais répondre dans cette partie au deux questions suivantes :

- **Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?**

- **Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?**

Le code présenté dans ce repo permet de manipuler et de traiter rapidement des petits jeux de données en CSV et JSON. La librairie pandas ne permettra pas de passer efficacement à l'échelle.

Une première étape consisterait à lancer le code sur des serveurs et à segmenter les différents traitement dans des pods. Chaque traitement aurait alors des ressources dédiés à son fonctionnement. Il faudrait aussi changer la librairie pandas pour que ces traitements soient plus efficaces. On pourrait utiliser des librairies comme Spark ou Flink.

Il faudrait ensuite réfléchir à une manière d'optimiser le stockage des données traitées. Les données d'entrées au format CSV et JSON pourraient simplement etre stocké sur un serveur dans un datalake. Il ne serait cependant pas efficace d'enregistrer les données de sortie au format JSON sur un serveur. Il me semble plus judicieux et pertinent d'utiliser une base de données en sortie. On pourrait utiliser une base de données NoSQL comme MongoDB pour s'adapter au format de sortie actuel de notre JSON.
