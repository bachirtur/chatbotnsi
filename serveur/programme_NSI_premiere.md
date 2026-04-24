## NSI programme de la classe de première

### Rubrique transversale de l’histoire de l’informatique

- **Événements clés de l’histoire de l’informatique**
  - Situer dans le temps les principaux événements de l’histoire de l’informatique et leurs protagonistes.
    > Ces repères historiques seront construits au fur et à mesure de la présentation des concepts et techniques. [commentaire]

### Représentation des données : types et valeurs de base

- **Écriture d’un entier positif dans une base b⩾2**
  - Passer de la représentation d’une base dans une autre.
    > Les bases 2, 10 et 16 sont privilégiées. [commentaire]
- **Représentation binaire d’un entier relatif**
  - Évaluer le nombre de bits nécessaires à l’écriture en base 2 d’un entier, de la somme ou du produit de deux nombres entiers.
    > Il s’agit de décrire les tailles courantes des entiers (8, 16, 32 ou 64 bits). [commentaire]
    >
    > Il est possible d’évoquer la représentation des entiers de taille arbitraire de Python. [commentaire]
  - Utiliser le complément à 2.
- **Représentation approximative des nombres réels : notion de nombre flottant**
  - Calculer sur quelques exemples la représentation de nombres réels : `0.1`, `0.25` ou $1/3$.
    > `0.2 + 0.1` n’est pas égal à `0.3`. [commentaire]
    >
    > Il faut éviter de tester l’égalité de deux flottants. [commentaire]
    >
    > Aucune connaissance précise de la norme IEEE-754 n’est exigible. [commentaire]
- **Valeurs booléennes : `0`, `1`.**
- **Opérateurs booléens : `and`, `or`, `not`.**
  > Le ou exclusif (`xor`) est évoqué. [commentaire]
  >
  > Quelques applications directes comme l’addition binaire sont présentées. [commentaire]
  >
  > L’attention des élèves est attirée sur le caractère séquentiel de certains opérateurs booléens. [commentaire]
- **Expressions booléennes**
  - Dresser la table d’une expression booléenne.
- **Représentation d’un texte en machine.**
- **Exemples des encodages ASCII, ISO-8859-1, Unicode**
  - Identifier l’intérêt des différents systèmes d’encodage.
    > Aucune connaissance précise des normes d’encodage n’est exigible. [commentaire]
  - Convertir un fichier texte dans différents formats d’encodage.

### Représentation des données : types construits

- **p-uplets.**
  - Écrire une fonction renvoyant un p-uplet de valeurs.
- **p-uplets nommés**
  - Écrire une fonction renvoyant un p-uplet de valeurs.
- **Tableau indexé, tableau donné en compréhension**
  > Seuls les tableaux dont les éléments sont du même type sont présentés. [commentaire]
  >
  > L’aspect dynamique des tableaux de Python n’est pas évoqué. [commentaire]
  >
  > Python identifie listes et tableaux. [commentaire]
  >
  > Il n’est pas fait référence aux tableaux de la bibliothèque NumPy. [commentaire]
  - Lire et modifier les éléments d’un tableau grâce à leurs index.
    > Aucune connaissance des tranches (slices) n’est exigible. [commentaire]
  - Construire un tableau par compréhension.
  - Utiliser des tableaux de compréhension tableaux pour représenter des matrices : notation `a[i][j]`.
  - Itérer sur les éléments d’un tableau.
- **Dictionnaires par clés et valeurs**
  - Construire une entrée de dictionnaire.
    > En Python, les p-uplets nommés sont implémentés par des dictionnaires. [commentaire]
  - Itérer sur les éléments d’un dictionnaire.
    > Il est possible de présenter les données EXIF d’une image sous la forme d’un enregistrement. [commentaire]
    >
    > Utiliser les méthodes `keys()`, `values()` et `items()`. [commentaire]

### Traitement de données en tables

- **Indexation de tables**
  - Importer une table depuis un fichier texte tabulé ou un fichier CSV.
    > Est utilisé un tableau doublement indexé ou un tableau de p-uplets qui partagent les mêmes descripteurs. [commentaire]
- **Recherche dans une table**
  - Rechercher les lignes d’une table vérifiant des critères exprimés en logique propositionnelle.
    > La recherche de doublons, les tests de cohérence d’une table sont présentés. [commentaire]
- **Tri d’une table**
  - Trier une table suivant une colonne.
    > Une fonction de tri intégrée au système ou à une bibliothèque peut être utilisée. [commentaire]
- **Fusion de tables**
  - Construire une nouvelle table en combinant les données de deux tables.
    > La notion de domaine de valeurs est mise en évidence. [commentaire]

### Interactions entre l’homme et la machine sur le Web

- **Modalités de l’interaction entre l’homme et la machine**
  - Identifier les différents composants graphiques permettant d’interagir avec une application Web.
    > Il s’agit d’examiner le code HTML d’une page comprenant des composants graphiques et de distinguer ce qui relève de la description des composants graphiques en HTML de leur comportement (réaction aux événements) programmé par exemple en JavaScript. [commentaire]
- **Événements**
  - Identifier les événements que les fonctions associées aux différents composants graphiques sont capables de traiter.
- **Interaction avec l’utilisateur dans une page Web**
  - Analyser et modifier les méthodes exécutées lors d’un clic sur un bouton d’une page Web.
- **Interaction client-serveur.**
  - Distinguer ce qui est exécuté sur le client ou sur le serveur et dans quel ordre.
- **Requêtes HTTP, réponses du serveur**
  > Il s’agit de faire le lien avec ce qui a été vu en classe de seconde et d’expliquer comment on peut passer des paramètres à un site grâce au protocole HTTP. [commentaire]
  - Distinguer ce qui est mémorisé dans le client et retransmis au serveur.
  - Reconnaître quand et pourquoi la transmission est chiffrée.
- **Formulaire d’une page Web**
  - Analyser le fonctionnement d’un formulaire simple.
  - Distinguer les transmissions de paramètres par les requêtes POST ou GET.
    > Discuter les deux types de requêtes selon le type des valeurs à transmettre et/ou leur confidentialité. [commentaire]

### Architectures matérielles et systèmes d’exploitation

- **Modèle d’architecture séquentielle (von Neumann)**
  > La présentation se limite aux concepts généraux. [commentaire]
  - Distinguer les rôles et les caractéristiques des différents constituants d’une machine.
    > On distingue les architectures monoprocesseur et les architectures multiprocesseur. [commentaire]
    >
    > Des activités débranchées sont proposées. [commentaire]
  - Dérouler l’exécution d’une séquence d’instructions simples du type langage machine.
    > Les circuits combinatoires réalisent des fonctions booléennes. [commentaire]
- **Transmission de données dans un réseau**
  - Mettre en évidence l’intérêt du découpage des données en paquets et de leur encapsulation.
- **Protocoles de communication**
  - Dérouler le fonctionnement d’un protocole simple de récupération de perte de paquets (bit alterné).
    > Le protocole peut être expliqué et simulé en mode débranché. [commentaire]
    >
    > Le lien est fait avec ce qui a été vu en classe de seconde sur le protocole TCP/IP. [commentaire]
- **Architecture d’un réseau**
  - Simuler ou mettre en œuvre un réseau.
    > Le rôle des différents constituants du réseau local de l’établissement est présenté. [commentaire]
- **Systèmes d’exploitation**
  - Identifier les fonctions d’un système d’exploitation.
    > Les différences entre systèmes d’exploitation libres et propriétaires sont évoquées. [commentaire]
    >
    > Il ne s’agit pas d’une étude théorique des systèmes d’exploitation. [commentaire]
  - Utiliser les commandes de base en ligne de commande.
    > Les élèves utilisent un système d’exploitation libre. [commentaire]
  - Gérer les droits et permissions d’accès aux fichiers.
- **Interface Homme-Machine (IHM) et périphériques d’entrée et de sortie [reformulé, ndr]**
  - Identifier le rôle des capteurs et actionneurs.
  - Réaliser par programmation une IHM répondant à un cahier des charges donné.
    > Les activités peuvent être développées sur des objets connectés, des systèmes embarqués ou robots. [commentaire]

### Langages et programmation

- **Constructions élémentaires**
  - Mettre en évidence un corpus de constructions élémentaires.
    > Séquences, affectation, conditionnelles, boucles bornées, boucles non bornées, appels de fonction. [commentaire]
- **Diversité et unité des langages de programmation**
  - Repérer, dans un nouveau langage de programmation, les traits communs et les traits particuliers à ce langage.
    > Les manières dont un même programme simple s’écrit dans différents langages sont comparées. [commentaire]
- **Spécification**
  - Prototyper une fonction.
  - Décrire les préconditions sur les arguments.
  - Décrire des postconditions sur les résultats.
  > Des assertions peuvent être utilisées pour garantir des préconditions ou des postconditions. [commentaire]
- **Mise au point de programmes**
  - Utiliser des jeux de tests.
    > L’importance de la qualité et du nombre des tests est mise en évidence. [commentaire]
    >
    > Le succès d’un jeu de tests ne garantit pas la correction d’un programme. [commentaire]
- **Utilisation de bibliothèques**
  - Utiliser la documentation d’une bibliothèque.
    > Aucune connaissance exhaustive d’une bibliothèque particulière n’est exigible. [commentaire]

### Algorithmique

- **Parcours séquentiel d’un tableau**
  > On montre que le coût est linéaire. [commentaire]
  - Écrire un algorithme de recherche d’une occurrence sur des valeurs de type quelconque.
  - Écrire un algorithme de recherche d’un extremum, de calcul d’une moyenne.
- **Tris par insertion, par sélection**
  > La terminaison de ces algorithmes est à justifier. [commentaire]
  >
  > On montre que leur coût est quadratique dans le pire cas. [commentaire]
  - Écrire un algorithme de tri.
  - Décrire un invariant de boucle qui prouve la correction des tris par insertion, par sélection.
- **Algorithme des k plus proches voisins**
  - Écrire un algorithme qui prédit la classe d’un élément en fonction de la classe majoritaire de ses k plus proches voisins.
    > Il s’agit d’un exemple d’algorithme d’apprentissage. [commentaire]
- **Recherche dichotomique dans un tableau trié**
  - Montrer la terminaison de la recherche dichotomique à l’aide d’un variant de boucle.
    > Des assertions peuvent être utilisées. [commentaire]
    >
    > La preuve de la correction peut être présentée par le professeur. [commentaire]
- **Algorithmes gloutons**
  - Résoudre un problème grâce à un algorithme glouton.
    > Exemples : problèmes du sac à dos ou du rendu de monnaie. [commentaire]
    >
    > Les algorithmes gloutons constituent une méthode algorithmique parmi d’autres qui seront vues en terminale. [commentaire]

