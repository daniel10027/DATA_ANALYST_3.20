#coding:utf-8

#creation d'une class

class codeur:
    ecole = "nan"
    nombre = 0
    def __init__(self, nom, prenom, langage, niveau):
        self.nom     = nom
        self.prenom  = prenom
        self.langage = langage
        self.niveau = niveau
        codeur.nombre +=1

    #methode standar 
    def coder(self,niveau):
        print("{} code en {} et a un niveau {}".format(nom,langage, niveau))
    #methode de class
    def changer_ecole(cls, nouvelle_ecole):
        codeur.ecole = nouvelle_ecole
    changer_ecole = classmethod(changer_ecole)
    #method static
    def ecole():
        print("Nan c'est cool")
    ecole = staticmethod(ecole)


print("ecole actuel {}".format(codeur.ecole))

codeur.changer_ecole("nan")
print("nouvelle ecole {}".format(codeur.ecole))
print(codeur.ecole)
