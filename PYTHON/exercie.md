````
# Les scripts du cours

1. 
    •Affectez les variables temps et distance par les valeurs 6.892 et 19.7.
    •Calculez et affichez la valeur de la vitesse.
    •Améliorez l’affichage en imposant un chiffre après le point décimal.
    
2. 
    •Saisissez un flottant. S’il est positif ou nul, affichez sa racine, sinon affichez un message
    d’erreur.
    
    •L’ordre lexicographique est celui du dictionnaire.
    Saisir deux mots, comparez-les pour trouver le « plus petit » et affichez le résultat.
    
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
    
4. 
    Initialisez deux entiers : a = 0 et b = 10.
    Écrire une boucle affichant et incrémentant la valeur de a tant qu’elle reste inférieure
    à celle de b.
    Écrire une autre boucle décrémentant la valeur de b et affichant sa valeur si elle est
    impaire. Boucler tant que b n’est pas nul.
    
5.
    Écrire une saisie filtrée d’un entier dans l’intervalle 1 à 10, bornes comprises. Affichez
    la saisie.
    
6.  Affichez chaque caractère d’une chaîne en utilisant une boucle for.
    Affichez chaque élément d’une liste en utilisant une boucle for.
  
7.  Affichez les entiers de 0 à 15 non compris, de trois en trois, en utilisant une boucle for
    et l’instruction range().

8.  Utilisez l’instruction break pour interrompre une boucle for d’affichage des entiers
   de 1 à 10 compris, lorsque la variable de boucle vaut 5.

9. Utilisez l’instruction continue pour modifier une boucle for d’affichage de tous entiers de 1 à 10 compris,
   sauf lorsque la variable de boucle vaut 5. 

10. demander a un utilisateur de saisr un nombre.
     essayez de soumettre une chaine de caractère .
     Vous avez une erreur ?
     A l'aide d'une exception gérez cette erreur.
     
11. Utilisez une exception pour calculer, dans une boucle évoluant de -3 à 3 compris, la
    valeur de sin(x)/x.
    

# Les Fonctions 


1. Écrire une procédure table avec quatre paramètres : base, debut, fin et inc.
   Cette procédure doit afficher la table des base, de debut à fin, de inc en inc.
   Tester la procédure par un appel dans le programme principal.
   
2. Écrire une fonction cube qui retourne le cube de son argument.
   Écrire une fonction volumeSphere qui calcule le volume d’une sphère de rayon r fourni
   en argument et qui utilise la fonction cube.
   Tester la fonction volumeSphere par un appel dans le programme principal.
   
3. Écrire une fonction maFonction, une fonction qui premet de resoudreune equation de type
   f (x) = ax2 + bx +c.
   seul la partie entiere des solution doit etre affichée
   
4. Écrire une fonction volMasseEllipsoide qui retourne le l'exentricité, le volume et la masse d’un ellipsoïde.
   Les paramètres sont les trois demi-axes. 
   On donnera à ces quatre paramètres des valeurs par défaut telle que rho = 11.2 .
   On donne : v =(4/3)πabc
   Tester cette fonction par des appels avec différents nombres d’arguments.

5
  .Écrire une fonction somme avec un argument « tuple de longueur variable » qui calcule
      la somme des nombres contenus dans le tuple.
      Tester cette fonction par des appels avec différents tuples d’entiers ou de flottants
      
6 .Écrire une autre fonction somme avec trois arguments, et qui renvoie leur somme.


# STRUCTURE DE DONNÉÉS


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

2. Initialisez truc comme une liste vide, et machin comme une liste de cinq flottants nuls.
    Affichez ces listes.
    Utilisez la fonction range() pour afficher :
    – les entiers de 0 à 3 ;
    – les entiers de 4 à 7 ;
    – les entiers de 2 à 8 par pas de 2.
    Définir chose comme une liste des entiers de 0 à 5 et testez l’appartenance des éléments 3 et 6 à chose.

3.  Utilisez une liste en compréhension pour obtenir la liste ['ad', 'ae', 'bd', 'be',
    'cd', 'ce'] à partir des chaînes "abc" et "de".
    

4. Définir deux ensembles (sets) : X = {a,b,c,d} et Y = {s,b,d}, puis affichez les résultats
  suivants :
    – les ensembles initiaux ;
    – le test d’appartenance de l’élément 'c' à X ;
    – le test d’appartenance de l’élément 'a' à Y ;
    – les ensembles X −Y et Y − X ;
    – l’ensemble X ∪Y (union) ;
    – l’ensemble X ∩Y (intersection).
    
5.  Écrire une fonction compterMots ayant un dictionnaire contenat plusieurs autre dictionnaire et qui
    renvoie la clé:la valeur de chaque dictionnaire .
```
