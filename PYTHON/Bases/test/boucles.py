#coding:utf-8

stop = 0

while not stop:
    nombre = int(input("Entrez un nombre\n"))

    if nombre <0:
        print('{} est inférieur à 0'.format(nombre))
    elif nombre >0:
        print('{} est superieur à 0'.format(nombre))
    else :
        print('{} est égal à 0 fin du jeu '.format(nombre))
        break