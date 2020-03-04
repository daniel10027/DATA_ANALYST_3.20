# CHAPITRE I : LA SELECTION DES ELEMENTS

En statistique, les données constituent le point de départ de toute analyse. Il est en effet très courant d’avoir à sélectionner une partie de nos données, soit en sélectionnant manuellement un sous-échantillon (par exemple les 30 premières lignes), soit selon une condition donnée (par exemple uniquement les femmes, ou les personnes de moins de 25 ans, etc.). Il est donc obligatoire de maîtriser les opérations de sélection simples que nous présentons ici.

### Principe de Sélection

Il y a deux grands principes dans la sélection d’éléments d’un objet R :
- la sélection par position : il faut indiquer un ou plusieurs vecteurs de positions (ou d’indices), des éléments à sélectionner;
- la sélection par condition : il faut indiquer une condition (qui pourra être construite via différents opérateurs de comparaison et des opérateurs logiques) et ne seront sélectionnés que les éléments satisfaisant cette condition.

Dans tous les cas, la sélection s’opère avec l’opérateur de sélection [ ].

#### La sélection par condition
Nous reviendrons un peu plus en détail dans les chapitres suivants sur la sélection par position, mais pour celle par condition, vous allez avoir besoin d’utiliser des opérateurs de comparaison pour construire vos conditions.

Comme le nom le suggère, les opérateurs de comparaison sont utilisés pour comparer deux valeurs. Il y en a six principaux :
==  égal à (deux valeurs sont exactement pareilles)

* !=  différent de
* <  inférieur à
* <=  inférieur ou égal
* >  supérieur à
* >=  supérieur ou égal
* %in%
* match()

Exemple : 

    x <- -4:5
    x > 0

On voit bien que le résultat est un vecteur de booléen, indiquant pour chaque élément si la condition est vraie ou non.
Parfois, vous allez avoir besoin de conditions plus élaborées, ou la condition va être le résultat de la combinaison de plusieurs expressions. C’est là qu’interviennent les opérateurs logiques.
Ces opérateurs vont vous permettre de mixer plusieurs valeurs booléennes : des valeurs booléennes spécifiques ou des résultats d’expression. Il y en a 3 :
- &  : l’opérateur ET.
Le résultat final est vrai seulement lorsque toutes les conditions sont vraies. Par exemple : le résultat de condition1 & condition2  sera à TRUE seulement si condition1  est vraie ET condition2  est également vraie.
- |  : l’opérateur OU.
Le résultat final est vrai lorsque au moins une des conditions est vraie. Par exemple : le résultat de condition1  | condition2  sera à TRUE si   condition1  est vraie OU condition2  est vraie.
- !  : l’opérateur N’EST PAS.
Cela inverse simplement le résultat de la condition donnée. Par exemple, le résultat de !(condition)  est vrai lorsque condition  est faux.

## En résumé
Il existe deux façons de sélectionner des éléments au sein d’un objet en R : soit via une sélection par position (ou indice), soit via une sélection par condition.

Les conditions peuvent être construites en utilisant des opérateurs de comparaisons et/ou des opérateurs logiques.

Maintenant que les différents principes de sélection sont claires, nous allons voir comment les mettre en œuvre avec des vecteurs !

#       CHAPITRE II : SELECTION DANS UN VECTEUR

La sélection au sein d’un vecteur s’opère avec l’opérateur de sélection  [ ]  et un vecteur de sélection :
    x[vecteurdeselection]
Le vecteur de sélection peut être un vecteur d’entiers positifs, d’entiers négatifs ou de logiques.

###  Selection par position
La sélection la plus naturelle est la sélection par des vecteurs d’entiers positifs. Les entiers sont les indices des éléments à sélectionner et doivent être compris entre 1 et la longueur du vecteur considéré (obtenue via la fonction length). La longueur du vecteur d’indices peut être quelconque :
    x <- c(2,-1,15)
    x[2] # donne le deuxième élément de x

    x[c(1,3)] # donne les premier et troisième éléments de x

    x[c(3,1,2,2,1)]

Une autre méthode consiste à enlever les éléments du vecteur que l’on ne souhaite pas conserver : c’est la sélection par des vecteurs d’entiers négatifs. Le vecteur d’indices indique les indices des éléments à exclure du résultat final :

    x[-2] # ne donne pas le deuxième élément de x

Une autre façon de procéder consiste à sélectionner des éléments du vecteur en fonction de leur valeur ou d’autres éléments provenant d’autres objets R. Cela conduit à la sélection par des vecteurs de logiques.

### Selection par condition
Cette sélection permet l’extraction d’éléments particuliers que l’on sait caractériser par une périphrase ou par une condition logique: « l’élément de sexe M » ou « l’élément qui possède une valeur inférieure à 5 et (ou) supérieure ou égale à 12 ».

    [x>0]
    
    x[!(x<0)]

Cependant, aucun élément n’est à la fois inférieur à 5 et supérieur à 12, la fonction retourne
alors l’ensemble vide avec  numeric(0)  :

    x[(x<5) & (x>=12)]

On peut aussi sélectionner les valeurs d’un vecteur à partir des valeurs d’un autre vecteur de même longueur :

    T <- c(23, 28, 24, 32)
    O3 <- c(80, 102, 87, 124)
    O3[T>25]

###  En résumé
Il est possible de sélectionner au sein d’un vecteur selon :

- un vecteur d’entiers positifs : dans ce cas, les entiers correspondent aux indices des éléments à sélectionner ;

- un vecteur d’entiers négatifs : dans ce cas, les entiers correspondent aux indices des éléments à exclure du résultat final ;

- une condition : dans ce cas, le résultat sera constitué de l’ensemble des éléments du vecteur initial qui satisfont cette condition.


#       CHAPITRE III : SELECTION DANS UNE MATRICE

L’emplacement d’un élément dans une matrice est en général donné par le numéro de sa ligne et de sa colonne. Ainsi, pour sélectionner l’élément  (i, j)  de la matrice  m  , il faut écrire :

    m[i,j]

Il est rare que l’on ait besoin de ne sélectionner qu’un seul élément dans une matrice. Usuellement, on sélectionne une ou plusieurs lignes et/ou une ou plusieurs colonnes. Voyons les différents cas rencontrés en pratique.

### Selection par Indice
Le premier cas est la sélection par des entiers positifs.

    m[i,]

Attention, cela retourne la ligne  i  sous la forme d’un vecteur. Pour conserver la structure de matrice il faut utiliser l’argument  drop :

    m[i,,drop=F]

Donne la ligne  i   sous la forme d’une matrice uniligne et non plus d’un vecteur, ce qui permet de conserver le nom de la ligne.

    m[,c(2,2,1)]

Donne deux fois la seconde, puis la première colonne : c’est donc une matrice à trois colonnes.

Tout comme avec les vecteurs, il est tout à fait possible de sélectionner avec des entiers négatifs:

    m[-1,] # matrice m sans sa première ligne
    m[1:2,-1] # 2 premières lignes de m privée de sa 1ère colonne

### Sélection par condition
Vous pouvez également sélectionner selon une condition, définie soit sur les lignes, soit sur les colonnes, voire les deux en même temps !

Soit la matrice  X  suivante :

    X <- matrix(1:12,nrow=3,ncol=4)

L’instruction suivante retourne uniquement les colonnes de  X  pour lesquelles la valeur sur la première ligne est strictement supérieure à 2 :

    X[,X[1,]>2]

C’est donc une matrice, alors que l’instruction suivante retourne un vecteur contenant les valeurs de  X  supérieures à 2 :

    X[X>2]

L’instruction suivante quant à elle remplace les valeurs de  X  inférieures à 5 par des NA

    X[X<5] <- NA

### En résumé
Il est possible de sélectionner au sein d’une matrice selon :

un entier positif ou un vecteur d’entiers positifs : pour pouvoir sélectionner en particulier une ligne ou une colonne. Un cas particulier est de spécifier un numéro de ligne et de colonne dans le cas où vous souhaiteriez ne sélectionner qu’un seul élément bien identifié ;

un entier négatif ou un vecteur d’entiers négatifs : pour exclure du résultat final les éléments dont les indices sont représentés par les entiers ;

une condition : définie soit sur les lignes, soit sur les colonnes, voire les deux en même temps.


#       CHAPITRE IV : SELECTION SUR LES LISTES

Pour extraire une composante de la liste, on peut toujours le faire en indiquant la position de l’élément que l’on souhaite extraire.

### Sélection par position
Les  [[ ]]  permettent de retourner l’élément de la liste.

Il faut faire la distinction entre :

- maliste[1]  qui retourne une sous-liste composée de l’élément 1 de la liste initiale. length(maliste[1])  vaut donc 1. 

- maliste[[1]]  qui retourne l’objet R qui compose l’élément 1 de la liste.length(maliste[[1]])  retourne la longueur de l’objet stocké en premier dans la liste  maliste.

Commençons par créer une liste de 4 éléments.
    x <- c("a","a","b","c")
    X <- matrix(1:8,ncol=4)
    y <- c(T,T,T,F,F)
    z <- matrix(c("A","B","C","D"),ncol=2)

    maliste <- list(comp1=x,comp2=X,comp3=y,element4=z)

Voyons à présent les différences notables entre la sélection avec l’opérateur [ ]  et celle avec l’opérateur [[ ]] au sein de notre liste de 4 objets:
    maliste[2] #retourne une liste

    length(maliste[2])

    maliste[[2]] #extrait le second élément de la liste

    length(maliste[[2]])

# puisqu’il y a 8 éléments dans la composante 2 de maliste.
On peut aussi utiliser le nom de l’élément s’il existe.

### Sélection par nom

Lorsque vous souhaitez sélectionner au sein d’une liste en utilisant directement le nom d’un des objets qu’elle contient, vous pouvez l’écrire de deux façons : soit de façon similaire à une sélection par position en précisant le nom entre quotes, soit via l’opérateur  $. Par exemple :

    maliste["comp2"]

    maliste[["comp2"]]

    maliste$comp2

Notez bien ici encore une fois la différence entre l’opérateur [ ] qui renvoie une sous-liste et l’opérateur [[ ]] qui renvoie l’objet que l’on souhaite sélectionner.

Il est possible d’extraire plusieurs éléments d’une même liste, ce qui crée une sous-liste. Noter qu’ici l’on utilise [ ] et non [[ ]] :

    maliste[c(1,3)]

### En résumé
Il existe différentes façons de sélectionner au sein d’une liste :

soit c’est une sélection par position. Cependant, il faut bien être vigilant à la différence entre une sélection via [ ] qui renverra une sous-liste de la liste originale et une sélection via  [[ ]] qui renverra l’objet stocké dans la liste à laquelle on essaie d’accéder ;

soit c’est une sélection par nom, où l’on peut accéder à une sous-liste ou un objet spécifique en utilisant le nom qui y est associé au sein de la liste.


#       CHAPITRE IV : SELECTION SUR LES DATAFRAMES

Tout comme la création, la sélection dans les dataframes est à mi-chemin entre la sélection dans les matrices et celle dans les listes. Commençons par créer un dataframe :
    
    x <- c("A","B","C",rep("D",3))
    y <- 1:6
    z <- c(seq(10,45,length=5),-10)
    df <- data.frame(x,y,z)
    df

### Sélection par position
Comme avec les matrices, il est possible de spécifier des lignes et/ou colonnes à sélectionner. Voici un exemple avec une sélection des 4 premières lignes et des colonnes 2 et 3 :

    df[1:4,2:3]

Nous pouvons, tout comme avec une liste, sélectionner via un nom associé à une colonne au sein du dataframe :

    df$z

    df["z"]

Il est également possible de pouvoir mixer les deux. Par exemple ici, nous sélectionnons les lignes 2 à 4 de la colonne  x  :

    df$x[2:4]

Notez ici que le vecteur de caractères a été automatiquement modifié en facteur par R lors de la création du dataframe. Si jamais vous souhaitez éviter cela, vous devrez préciser l’argument  stringsAsFactors = FALSE  lors de la création du dataframe !

### Sélection par condition
Même s’il arrive de sélection par indice, il est généralement plus courant de devoir sélectionner selon une condition.

Par exemple, la ligne suivante permet de sélectionner toutes les lignes qui satisfont la condition spécifiée :

    df[df$y>4,]

    df[(df$y>4)|(df$z>17),]

    df[(df$y>4)&(df$z>17),]

Vous noterez que, lors de la construction de vos conditions, il est indispensable de repréciser l’association  dataframe$colonne, même si le nom associé à une colonne d’un dataframe est forcément unique. Vous pouvez également préciser une ou plusieurs colonnes en particulier :

    df[df$y>4,1:2] # équivalent à
    df[df$y>4,c('x','y')]

En résumé
Le dataframe étant un objet à mi-chemin entre une liste et une matrice, il partage les façons de sélectionner de ces deux types :

- Vous pouvez sélectionner selon un indice ou un vecteur d’indice, sur les lignes, les colonnes ou les deux en même temps.

- Vous pouvez sélectionner en précisant le nom associé à la colonne d’un dataframe.

- Vous pouvez sélectionner selon une condition qui ne va conserver que les lignes qui satisfont ladite condition.

- Et il est tout à fait possible de mixer ces différentes méthodes pour arriver à une sélection bien précise !