
# Les scripts du cours

```
1. 
    •Affectez les variables temps et distance par les valeurs 6.892 et 19.7.
    •Calculez et affichez la valeur de la vitesse.
    •Améliorez l’affichage en imposant un chiffre après le point décimal.
````

    
2. 
    •Saisissez un flottant. S’il est positif ou nul, affichez sa racine, sinon affichez un message
    d’erreur.
    
    •L’ordre lexicographique est celui du dictionnaire.
    Saisir deux mots, comparez-les pour trouver le « plus petit » et affichez le résultat.
```    
3.
    On désire sécuriser une enceinte pressurisée.
    On se fixe une pression seuil et un volume seuil : pSeuil = 2.3, vSeuil = 7.41.
    On demande de saisir la pression et le volume courant de l’enceinte et d’écrire un script
    qui simule le comportement suivant :
    – si le volume et la pression sont supérieurs aux seuils : arrêt immédiat ;
    – si seule la pression est supérieure à la pression seuil : demander d’augmenter le volume de l’enceinte ;
    – si seul le volume est supérieur au volume seuil : demander de diminuer le volume
    de l’enceinte ;
    – sinon déclarer que « tout va bien ».
 ````

```
4. 
    Initialisez deux entiers : a = 0 et b = 10.
    Écrire une boucle affichant et incrémentant la valeur de a tant qu’elle reste inférieure
    à celle de b.
    Écrire une autre boucle décrémentant la valeur de b et affichant sa valeur si elle est
    impaire. Boucler tant que b n’est pas nul.
```

```    
5.
    Écrire une saisie filtrée d’un entier dans l’intervalle 1 à 10, bornes comprises. Affichez
    la saisie.
```
```
  
6.  Affichez chaque caractère d’une chaîne en utilisant une boucle for.
    Affichez chaque élément d’une liste en utilisant une boucle for.
 ````
````
 
7.  Affichez les entiers de 0 à 15 non compris, de trois en trois, en utilisant une boucle for
    et l’instruction range().
````

````
8.  Utilisez l’instruction break pour interrompre une boucle for d’affichage des entiers
   de 1 à 10 compris, lorsque la variable de boucle vaut 5.
````

````
9. Utilisez l’instruction continue pour modifier une boucle for d’affichage de tous entiers de 1 à 10 compris,
   sauf lorsque la variable de boucle vaut 5. 
````

````
10. demander a un utilisateur de saisr un nombre.
     essayez de soumettre une chaine de caractère .
     Vous avez une erreur ?
     A l'aide d'une exception gérez cette erreur.
````  


````    
11. Utilisez une exception pour calculer, dans une boucle évoluant de -3 à 3 compris, la
    valeur de sin(x)/x.
````    

# Les Fonctions 

````
1. Écrire une procédure table avec quatre paramètres : base, debut, fin et inc.
   Cette procédure doit afficher la table des base, de debut à fin, de inc en inc.
   Tester la procédure par un appel dans le programme principal.
````

````

2. Écrire une fonction cube qui retourne le cube de son argument.
   Écrire une fonction volumeSphere qui calcule le volume d’une sphère de rayon r fourni
   en argument et qui utilise la fonction cube.
   Tester la fonction volumeSphere par un appel dans le programme principal.
 ````
````

3. Écrire une fonction maFonction, une fonction qui premet de resoudreune equation de type
   f (x) = ax2 + bx +c.
   seul la partie entiere des solution doit etre affichée
 `````
 
`````
4. Écrire une fonction volMasseEllipsoide qui retourne le l'exentricité, le volume et la masse
d’un ellipsoïde.
   Les paramètres sont les trois demi-axes. 
   On donnera à ces quatre paramètres des valeurs par défaut telle que rho = 11.2 .
   On donne : v =(4/3)πabc
   Tester cette fonction par des appels avec différents nombres d’arguments.
`````
````
`````
5
  .Écrire une fonction somme avec un argument « tuple de longueur variable » qui calcule
      la somme des nombres contenus dans le tuple.
      Tester cette fonction par des appels avec différents tuples d’entiers ou de flottants
 `````

````
6 .Écrire une autre fonction somme avec trois arguments, et qui renvoie leur somme.

`````

# STRUCTURE DE DONNÉÉS

````
1. définir la liste : liste =[17, 38, 10, 25, 72], puis effectuez les actions suivantes :
      – triez et affichez la liste ;
      – ajoutez l’élément 12 à la liste et affichez la liste ;
      – renversez et affichez la liste ;
      – affichez l’indice de l’élément 17 ;
      – enlevez l’élément 38 et affichez la liste ;
      – affichez la sous-liste du 2eau 3eélément ;
      – affichez la sous-liste du début au 2eélément ;
      – affichez la sous-liste du 3eélément à la fin de la liste ;
      – affichez la sous-liste complète de la liste ;
      – affichez le dernier élément en utilisant un indiçage négatif.
`````

````
2. Initialisez truc comme une liste vide, et machin comme une liste de cinq flottants nuls.
    Affichez ces listes.
    Utilisez la fonction range() pour afficher :
    – les entiers de 0 à 3 ;
    – les entiers de 4 à 7 ;
    – les entiers de 2 à 8 par pas de 2.
    Définir chose comme une liste des entiers de 0 à 5 et testez l’appartenance des éléments 3 et 6 à chose.
`````

`````
3.  Utilisez une liste en compréhension pour obtenir la liste ['ad', 'ae', 'bd', 'be',
    'cd', 'ce'] à partir des chaînes "abc" et "de".
 `````
 
````
4. Définir deux ensembles (sets) : X = {a,b,c,d} et Y = {s,b,d}, puis affichez les résultats
  suivants :
    – les ensembles initiaux ;
    – le test d’appartenance de l’élément 'c' à X ;
    – le test d’appartenance de l’élément 'a' à Y ;
    – les ensembles X −Y et Y − X ;
    – l’ensemble X ∪Y (union) ;
    – l’ensemble X ∩Y (intersection).
`````
````

5.  Écrire une fonction compterMots ayant un dictionnaire contenat plusieurs autre dictionnaire et qui
    renvoie la clé:la valeur de chaque dictionnaire .
 ````   
 
# Modules et fichiers

 
        Écrire un module de calcul des racines du trinôme réel : ax2 +bx +c.
        Le module définit une fonction trinome avec les trois paramètres du trinôme, a, b et
        c. La fonction doit retourner un tuple dont le premier élément est le nombre de racines
        du trinôme (0, 1 ou 2), et les autres éléments sont les racines éventuelles.
        Testez votre fonction avec les trois jeux de valeurs suivantes : 1,−3, 2, 1,−2, 1 et 1, 1, 1.


# Programmation Orientée Objet

````
1. Définir une classe MaClasse possédant les attributs suivants :
   données : deux attributs de classes : x = 23 et y = x + 5.
   méthode : une méthode affiche contenant un attribut d’instance z = 42 et les affichages de y et de z.
   Dans le programme principal, instanciez un objet de la classe MaClasse et invoquez la
   méthode affiche.
````




# EXERCICE DE PERFECTIONNEMENT 

````
Énoncés

. Un permis de chasse à points remplace désormais le permis de chasse traditionnel.
Chaque chasseur possède au départ un capital de 100 points. S’il tue une poule il perd
1 point, 3 points pour 1 chien, 5 points pour une vache et 10 points pour un ami. Le
permis coûte 200 euros.
Écrire une fonction amende qui reçoit le nombre de victimes du chasseur et qui renvoie
la somme due.
Utilisez cette fonction dans un programme principal qui saisit le nombre de victimes
et qui affiche la somme que le chasseur doit débourser.


. Je suis ligoté sur les rails en gare d’Arras. Écrire un programme qui affiche un tableau
me permettant de connaître l’heure à laquelle je serai déchiqueté par le train parti de
la gare du Nord à 9h (il y a 170 km entre la gare du Nord et Arras).
Le tableau prédira les différentes heures possibles pour toutes les vitesses de 100 km/h
à 300 km/h, par pas de 10 km/h, les résultats étant arrondis à la minute inférieure.
– Écrire une procédure tchacatchac qui reçoit la vitesse du train et qui affiche l’heure
du drame ;
– écrire le programme principal qui affiche le tableau demandé.
11. Un programme principal saisit une chaîne d’ADN valide et une séquence d’ADN va- ▹
lide (« valide » signifie qu’elles ne sont pas vides et sont formées exclusivement d’une
combinaison arbitraire de "a", "t", "g" ou "c").
Écrire une fonction valide qui renvoie vrai si la saisie est valide, faux sinon.
Écrire une fonction saisie qui effectue une saisie valide et renvoie la valeur saisie sous
forme d’une chaîne de caractères.
Écrire une fonction proportion qui reçoit deux arguments, la chaîne et la séquence et
qui retourne la proportion de séquence dans la chaîne (c’est-à-dire son nombre d’occurrences).
Le programme principal appelle la fonction saisie pour la chaîne et pour la séquence
et affiche le résultat.
Exemple d’affichage :
Il y a 13.33 % de "ca" dans votre chaîne.

12. Il s’agit d’écrire, d’une part, un programme principal, et d’autre part, une fonction utilisée dans le programme principal.
L’utilisateur remplit un tableau de N = 100 entiers avec des entiers aléatoires en utilisant une fonction randint(a,b) qui retourne un entier entre a et b −1. Une fonction
nommée indiceDuMin() reçoit ce tableau et retourne l’indice de la case qui contient
le minimum.
Écrire la fonction indiceDuMin().
Écrire le programme qui échange le premier élément du tableau avec le minimum de
ce tableau.

13. Un tableau t ab comporte N = 100 variables flottantes dont les n premières (n < 100)
sont utilisées.
BC v2.1 - 9 - 2008 - 2009
Énoncés
Écrire une fonction indiceDuMax() qui retourne l’indice du plus grand flottant parmi
ces n, et une autre indiceDuMin() qui retourne l’indice du plus petit.
Écrire ensuite un programme principal effectuant les actions suivantes :
– saisie filtrée de n (vous devez faire en sorte que n ne puisse pas être saisi hors de ses
limites) ;
– remplissage aléatoire des n premières valeurs de t ab (on utilisera le module random(),
sans argument, qui retourne un flottant au hasard entre 0.0 et +1.0) ;
– affichage de l’amplitude du tableau (écart entre sa plus grande et sa plus petite valeur) ;
– affichage de la moyenne des n premières valeurs de t ab.
14. Écrire une fonction conv() qui reçoit deux paramètres, une température et un entier
n, et qui retourne la conversion Celsius → Fahrenheit (n = 1), ou Fahrenheit → Celsius
(n = 2).

Rappel : TF = 32+1.8×TC

15. Fonction renvoyant plusieurs valeurs sous forme d’un tuple.
Écrire une fonction minMaxMoy qui reçoit une liste d’entiers et qui renvoie le minimum,
le maximum et la moyenne de cette liste. Le programme principal appellera cette fonction avec la liste : [10, 18, 14, 20, 12, 16].

16. Saisir un entier entre 1 et 3999 (pourquoi cette limitation ?). L’afficher en nombre romain.
◃ 17. Améliorer le script précédent en utilisant la fonction zip().

◃ 18. Un tableau contient n entiers (2 < n < 100), tous compris entre 0 et 500. Vérifier qu’ils
sont tous différents.

19. L’utilisateur donne un entier n entre 2 et 12, le programme donne le nombre de façons
de faire n en lançant deux dés.

20. Même problème que le précédent mais avec n entre 3 et 18 et trois dés
