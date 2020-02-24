#coding:utf-8


nombre = int(input("Entrez un nombre\n"))

if nombre <0:
    print('{} est inférieur à 0'.format(nombre))
elif nombre >0:
    print('{} est superieur à 0'.format(nombre))
else :
    print('{} est égal à 0'.format(nombre))