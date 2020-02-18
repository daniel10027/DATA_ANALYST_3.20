# INTRODUCTION À DOCKER
![docker](https://github.com/daniel10027/DATA_ANALYST_3.20/blob/master/11507000.webp)

    Docker est un projet open source (Apache 2.0) écrit en GO et hébergé sur GitHub:
https://github.com/docker (https://github.com/docker).
Initialement porté par la startup DotCloud (renommée depuis Docker) fondée par
deux français anciens de l’Epitech.
Docker est composé de trois éléments :
- le daemon Docker qui s’exécute en arrière-plan et qui s’occupe de gérer les
conteneurs (Containerd avec runC)
- Une API de type REST qui permet de communiquer avec le daemon
- Le client en CLI (command line interface) : commande docker

    Par défaut, le client communique avec le daemon Docker via un socket Unix
(/var/run/docker.sock) mais il est possible d’utiliser un socket TCP.
Docker c’est aussi un dépôt d’images (aussi appelé registry) :
https://store.docker.com (https://store.docker.com)
Il contient les images officielles maintenues par Docker mais aussi celles mises à
disposition par d’autres contributeurs.

Quelques concepts:
- une image est un ensemble de fichiers inertes en read-only.
- Un conteneur est une instance une active (started) ou inactive (stopped) d’une
image. L’execution d’un conteneur n’altère jamais une image.


LEXIQUE
- Conteneur : Image exécutable d’un environnement complet incluant code,
librairies, outils et configuration
- Image : template de conteneur en read-only contenant un systeme de base et
une application.
- Docker HUB : Dépôt public d’images mises à disposition par Docker
DockerHub (https://store.docker.com)
- Dockerfile : fichier texte de description d’une image
- Docker Compose : fichier texte (yaml) de description d’un ensemble de
conteneurs
- Docker Machine : Outil de déploiement des hôtes Docker sur différentes
plateformes (Mac, Windows) : https://docs.docker.com/machine/overview/
(https://docs.docker.com/machine/overview/)
- Orchestrateur : gère un pool de ressources serveurs ( Swarm, Kubernetes,
Mesos, Rancher…)
- Registry : Dépôt privé d’images Docker

