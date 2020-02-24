# CHAPITRE 1 : PRENEZ EN MAIN R ET RSTUDIO

- Vous pouvez utiliser R tout seul, ou de préférence grâce à l’environnement de développement RStudio.
- Vous avez vu comment ouvrir une session et faire vos premiers pas sur R.
- Vous avez vu comment utiliser l’aide de R et comment installer des nouveaux packages.
Et voilà, votre environnement de travail est installé, voyons à présent les différents types d'objet que 
vous allez manipuler au quotidien, dans le prochain chapitre.


#      CHAPITRE II : LES DIFFERENTS TYPES D'OBJETS EN R

Il existe de nombreux objets permettant de représenter au mieux la réalité (vecteurs, matrices, etc.). 
R possède de nombreuses fonctions et opérateurs qui facilitent la manipulation de ces derniers. 
Dans cette partie, Voyons ainsi comment créer et manipuler ces différents objets.

####    Les types d'éléments
    En R un objet est composé d'élements et les principaux types d'élements sont :
- Numérique : correspond à toute valeur numérique (entier, décimal et réel)
- Complex :  permettant de représenter des nombres complexes
- Caractères : chaîne de caractères, permettant de stocker du texte
- Booléens : booléen, permettant des opérations logiques. 
- Nul : représentant le vide, lorsqu’il n’y a rien : NULL

#### Les Objets

    Un objet R est en général une collection d'éléments. Il existe deux grandes familles d'objets :
- Objets monotypes 
- Objets de types differents 
    Tout objet a deux attributs intrinsectes : 
    - Sa longueur,
    - Son mode.

#### Les Listes
    En général la liste est un collection d'objets (Ex : vecteurs, matrices, liste)

#### Les DataFrames

    lE DataFrames est l'objet statistique par nature. Une liste particulière dont tous les éléments sont des 
vecteur de meme longueurs

### Créer des Objets 

Avant de pouvoir utiliser un objet, il faut pouvoir le créer : pour cela, l’affectation - le fait d’associer une valeur, un objet bien particulier à un nom, de créer une variable - peut se faire via trois opérateurs:<-,->ou=. 
Voici comment les utiliser en pratique : 
    x <- "Language r" : Créé l'objet x en lui donnant en lui donnant comme valeur la chaine de Caractères "Languae r".
    X = 5 : L'objet X reçoit la valeur 5; X et x sont deux objet differents
    3 -> obj : L'objet obj reçoit la valeur 3

Les trois opérateurs ci-dessus sont autorise mais seul la première est conseillé.

### Manipulez les types d’objets 

- La comande rm(obj) pour remove : permet de supprimer l'objet obj
- La commande length(x) pour longeur : permet de donner la longueur de l'objet x
- La commande mode(x) pour le type :  permet de donner le type de l'objet x

### Resumé

Vous pouvez créer des objets via une opération d’affectation.

- Il est possible d’ajouter des commentaires ne servant qu’à la documentation du code.
- Vous pouvez contrôler l’environnement en affichant ou supprimant vos objets.
- Il existe cinq types (ou modes) d’objets fondamentaux :null, logical, numeric, complex et character.
- Vous pouvez réaliser une conversion pour changer le type d’un objet.
- Les valeurs manquantes sont représentées par des  NA  en R.


# CHAPITRE III : UTILISER LES VECTEURS 

Le vecteur est une sorte de tableau d’une ligne (ou une colonne) pouvant stocker plusieurs valeurs appelées composantes, coordonnées ou éléments. C’est un objet monotype: tous les éléments d’un vecteur sont donc du même type. Tout comme chaque objet, on peut obtenir l’attribut longueur (correspondant au nombre d’éléments contenus dans un vecteur) via la fonction  length  .

### Les Vecteurs Numériques

Les vecteurs numériques vont permettre de représenter numériquement toutes les séries de nombres que vous pourrez rencontrer lors de vos analyses : relevés météorologiques, notes d’une classe, taille de différentes fleurs, etc. De façon générale, ils vont permettre de représenter toutes vos variables quantitatives.

Il existe différentes méthodes pour construire un vecteur, que vous pouvez utiliser en fonction de vos besoins :

Construction par l’opérateur séquence  :. Ce dernier permet de créer un vecteur allant de la première valeur à la deuxième, par pas de 1.

   -3:5

Construction par la fonction  seq, qui va créer un vecteur contenant l’ensemble des valeurs de a à b, soit répartis également si l’on utilise l’argument length, soit selon un pas donné via l’argument by.

   seq(1,6,by=0.5)

   seq(1,6,length=5)

Construction par la fonction collecteur c. Cette dernière permet de construire un vecteur en citant explicitement l’ensemble des valeurs que l’on stocke à l’intérieur.

    v1 <- c(1, 4, 10) # vecteur de numériques à 3 éléments

    v2 <- seq(1,10,by=2) # vecteur à 7 éléments

    v3 <- c(x,y)

Construction par la fonction  rep, qui va répéter un objet (valeur seule, vecteur, etc.) un nombre de fois fixé.

    rep(1,4)

    rep(c(1,4),each=5)

    rep(c(1,3),times=5)

Il est possible de concatener deux vecteur v1 et v2 avec la meme commande c:
    v5 = c(v1,v2)


### Les vecteurs de caractères
Les vecteurs de caractères vont eux représenter toutes les séries d’informations textuelles comme : les noms de stations météo, les noms des élèves, les espèces de fleurs, etc. De façon globale, ils permettront de représenter des variables qualitatives.

Il est possible de créer des vecteurs de caractères de la même façon que des vecteurs numériques, en utilisant les fonctions c ou rep.

#### Création par concaténation
Une autre façon de procéder, pour créer un vecteur de caractères, est de manipuler différents objets R et de les concaténer (c’est-à-dire les mettre bout à bout) ou d’en extraire une partie. Pour la concaténation, on utilise la fonction  paste :

    nom <- paste(rep("ind",10),1:10,sep=".")
    
    paste(c("X","Y"),1:5,sep=".",collapse="+")
    
L’argument  collapse  permet de concaténer l’ensemble des éléments d’un vecteur en un seul, délimités par le caractère passé en argument. Par exemple, ci-dessus, le résultat correspond à l’ensemble des valeurs du vecteur mises bout à bout, entrecoupées par le caractère +.

Pour faire extraction, on utilise la fonction substr.
    substr("freerider",5,9)  
Cela extrait de "freerider" les caractères en position 5 à 9 ce qui donne "rider".


### Vecteurs logiques
Les vecteurs logiques sont un peu particuliers en pratique. Ils peuvent représenter des vecteurs binaires (pluie ou beau temps, présence ou non d’une maladie, etc.), mais peuvent aussi être le résultat d’une fonction appliquée à un autre vecteur (comme avec la fonction  is.na  vue précédemment).

Les vecteurs de booléens sont en général générés grâce à des opérateurs logiques : >  ,  >=, <, <=, ==, !=, etc. Ils peuvent aussi être générés par les fonctions  seq, rep et c. Ils permettent des sélections complexes ou des opérations de conditions.

x>13 retourne un vecteur logique de même longueur que  x. Ses éléments ont la valeur TRUE quand l’élément correspondant satisfait la condition (ici strictement supérieur à 13) et la valeur FALSE s’il ne la satisfait pas. Lors d’opérations arithmétiques, les logiques sont transformées en numériques avec la convention selon laquelle les FALSE sont transformés en 0 et les TRUE en 1.

Voyons cela sur un exemple. Nous créons un objet test qui est le vecteur de logiques (FALSE,FALSE,TRUE), puis nous calculons le produit suivant :

    x <- c(-2,0,2)
    test <- x>1
    (1+x^2)*(x>1)

On peut aussi utiliser les fonctions  all  ou  any  . La fonction  all  renvoie TRUE si tous les éléments satisfont la condition et FALSE sinon. La fonction  any  renvoie TRUE dès que l’un des éléments satisfait la condition, FALSE sinon.

    all(x>1)

    any(x>1)

### En résumé
Un vecteur permet de pouvoir stocker plusieurs éléments d’un même type. On peut ainsi avoir :
- Des vecteurs de numériques
- Des vecteurs de caractères
- Des vecteurs logiques
Il existe plusieurs façons de créer un vecteur, soit via l’opérateur :, soit via une fonction adéquate. Vous pouvez convertir un vecteur d’un type à un autre, en utilisant la fonction adéquate.


# CHAPITRE IV : UTILISER LES FACTEURS

Les facteurs sont des vecteurs un peu particuliers, facilitant la manipulation de données qualitatives (qu’elles soient numériques ou caractères). En effet, en plus de stocker les différents éléments comme un vecteur classique, il stocke également l’ensemble des différentes modalités possibles dans un attribut accessible via la commande  levels  .

Ils forment une classe d’objets et bénéficient de traitements particuliers lors de leur manipulation et lors de l’utilisation de certaines fonctions. Les facteurs peuvent être non ordonnés (homme, femme) ou ordonnés (niveaux de ski).


### Création de facteurs
Il existe trois fonctions permettant de créer les facteurs.

#### Les fonctions factor et as.factor
Ces deux fonctions sont très similaires dans leur utilisation. La première permet de créer un facteur en définissant directement les différents éléments du facteur, l’autre permet de transformer un autre objet en facteur. Dans tous les cas, ces deux fonctions permettent généralement de créer des facteurs non ordonnés.

    fonction <- c("Eleve","Eleve","Etudiant","Eleve","etudiant")
    fonction_facteur <- factor(fonction)

Il est possible de regarder les attributs de ce fonction_facteur.
attributes(fonction_facteur) 

    levels(fonction_facteur) 

    nlevels(fonction_facteur)

Il y a aussi possibilités de renomer les modalités lors de la constructiondu facteur

levels(fonction_facteur) <- c("Eleve","Universitaire")

Il est possible de faire ce changement de nom à l’intérieur de la fonction factor avec l’argument  labels.

#### La fonction ordered
La fonction  ordered  va quant à elle nous permettre de créer des facteurs ordonnés.

Pour avoir un apperçu sur une variable ou un resumé de celle-ci, on utilise la fonction summary()
    summary(fonction_facteur)


### En résumé
Le facteur est un objet permettant de représenter au mieux une variable qualitative.
Il permet de garder en mémoire :
l’ensemble des éléments, comme un vecteur ;
les différentes modalités possibles.
Les modalités d’un facteur peuvent être ordonnées ou non.
Il n’est pas possible d’ajouter un élément qui n’est pas défini dans les différentes modalités (levels).
Vous pouvez convertir un vecteur en facteur et inversement, en utilisant les fonctions adéquates.


# CHAPITRE V : LES MATRICES

Les matrices - équivalentes aux matrices en mathématiques - peuvent être vues comme des tableaux de valeurs, à double entrée. Une matrice est donc définie par son nombre de lignes et de colonnes. Ce sont des objets monotypes, c’est-à-dire de même type pour tous ses éléments. Chaque valeur de la matrice peut être repérée par son numéro de ligne et son numéro de colonne. Les deux attributs intrinsèques d’un objet R sont la longueur  length  , qui correspond ici au nombre total d’éléments de la matrice, et le mode  mode  , qui correspond ici au mode des éléments de cette matrice. Les matrices possèdent également l’attribut de dimension  dim  , qui retourne le nombre de lignes et le nombre de colonnes.

### Création d'Une Matrice

Voici les principales façons de créer une matrice. La plus utilisée est la fonction  matrix  qui prend en arguments le vecteur d’éléments et les dimensions - nombre de lignes ou de colonnes - de la matrice. Par défaut, R range les valeurs dans une matrice par colonne. Pour ranger les éléments par ligne, on utilise l’argument  "byrow"  :

    x <- matrix(c(1:6),nrow=2,ncol=3,byrow=TRUE)

    y <- matrix(1:2,ncol=1)

    z <- matrix(3:1,ncol=3)

NB : Par defaut un vecteur n'est pas un matrice. Cependant, il est possible de le convertir en matrice en utilisant la methode : as.matrix()

### Opération sur les matrices 
Soit m <- matrix(1:4,ncol=2) et n <- matrix(3:6,ncol=2,byrow=T) deux matrices
- Somme : m+n (Vous pouvez additionner deux matrices de même dimension)
- Multiplication : m*n (On calculer le produit entre deux matrices, lorsque le nombre de lignes de la première est égal au nombre de colonnes de la deuxième.)
- sin(m) (sinus élément par élément)
- exp(m) (exponentielle élément par élément)
- m^4 (puissance quatrième élément par élément) 
- etc.

#### Quelques fonctions utiles

- Dimensions : dim(), nrow(), ncol()
- Concatenation : cbind(), rbind()
- apply()

### En résumé
Les matrices sont des sortes de tableaux monotypes à deux dimensions où chaque élément est identifié par son numéro de ligne et son numéro de colonne.

Vous pouvez créer une matrice soit à partir d’un objet existant (vecteur notamment), soit en définissant directement les éléments via la fonction matrix.

Vous pouvez réaliser de nombreuses opérations d’algèbre linéaire via différents opérateurs ou fonctions.

Il existe plusieurs fonctions permettant d’accéder aux dimensions (nombre de lignes, nombre de colonnes, etc.) et/ou de concaténer des matrices.

Maintenant que nous savons comment créer une matrice, nous allons voir comment créer des listes.

# CHAPITRE VI : LES LISTES

Lors de vos analyses statistiques, vous risquez d’être confronté à la gestion de plusieurs données de types différents et potentiellement de longueurs différentes. Bien entendu, vous pourriez stocker tous ces éléments dans autant de vecteurs/variables/facteurs en fonction de vos besoins. Mais ne serait-il pas plus pratique d’avoir un seul objet permettant de stocker tous ces différents objets ? C’est ce à quoi correspondent les listes.

Une liste est un ensemble ordonné d’objets qui n’ont pas toujours le même mode ou la même longueur. Les différents objets sont appelés des composantes et peuvent être associés à un nom spécifique (un peu comme une variable). Les listes ont les deux attributs des vecteurs (length et mode) et l’attribut supplémentaire names. Les listes sont des objets indispensables, car toutes les fonctions qui retournent plusieurs objets le font sous la forme d’une liste.

### Création de listes
La fonction de base pour créer une liste est la fonction list :
    ma_liste <- list(c("Je", "Suis", "NaNien", "3.20"), matrix(1:4,2,2))

Comme dit plus tôt, vous pouvez nommer les composantes de la liste, c’est-à-dire associer un nom à chaque objet de la liste pour pouvoir y accéder plus facilement via l’opérateur $. Ceci est faisable via la fonction  names().


### Fonctions utiles applicables sur des listes
Comme les objets d’une liste n’ont pas forcément le même type, il n’est pas possible de faire des calculs entre plusieurs listes. Néanmoins, il existe quelques fonctions valides et utiles :

- lapply  applique une fonction (comme la moyenne, la variance, etc.) successivement à chacune des composantes.

- unlist(maliste)  crée un seul vecteur contenant tous les éléments de la liste. Les éléments d’un vecteur étant nécessairement du même mode, il faut faire attention à la conversion automatique pratiquée par R.

- c(liste1,liste2)  concatène deux listes.

### En résumé
- Une liste est un ensemble ordonné d’objets qui n’ont pas toujours le même mode ou la même longueur.

- Il est possible d’associer un nom à un objet spécifique de la liste.

- Plusieurs fonctions permettent d’effectuer une action sur chaque élément d’une liste.


#   CHAPITRE VII : LES DATAFRAMES

Les dataframes sont des listes particulières dont les composantes sont de même longueur, mais les modes peuvent être différents. C’est d’ailleurs l’objet privilégié en analyse statistique : en effet, un tableau de données est constitué de variables quantitatives et/ou qualitatives mesurées sur les mêmes individus.

### Création d'un dataframe

Les principales manières de créer un dataframe consistent à utiliser les fonctions :
- data.frame  qui permet de concaténer des vecteurs de même taille et éventuellement de modes différents ;
- read.table  qui permet d’importer un tableau de données provenant d’un fichier externe (csv, txt, etc.)
- as.data.frame  pour la conversion explicite d’un objet à deux dimensions (comme une matrice).
Considérons les deux vecteurs  x  et  y  suivants :
    v1 <- c("Je", "Suis", "NaNien", "3.20")
    v2 <- 1:4

On peut créer un dataframe assemblant ces deux vecteurs
df <- data.frame(v1,v2)

Il est possible de transformer une matrice en dataframe en utilisant la fonction  as.data.frame. Il est aussi possible de faire le contraire en utilisant la fonction  data.matrix.

### En résumé
- Vous pouvez créer un dataframe à partir d’un objet à deux dimensions déjà existant (comme une matrice) ou via l’importation d’un fichier externe (csv, txt, etc.).

- Il est possible d’afficher un dataframe dans une fenêtre externe, pour faciliter sa visualisation.

Félicitation ! Vous connaissez à présent tous les objets natifs de R qui sont indispensables à l'analyse statistique. Nous allons voir à présent comment sélectionner concrètement au sein de ces objets dans la prochaine partie.