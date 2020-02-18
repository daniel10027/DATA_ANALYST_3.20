# INTRODUCTION À DOCKER

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

### Quelques concepts:
- une image est un ensemble de fichiers inertes en read-only.
- Un conteneur est une instance une active (started) ou inactive (stopped) d’une
image. L’execution d’un conteneur n’altère jamais une image.


### LEXIQUE
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


### LES CONTENEURS
Un conteneur linux est unprocessus ou  un ensemble de processus isolés du reste du système, tout en étant légers.

     ---- LES AVANTAGES DES CONTENEUR --
- Pas de reserve de ressources nécéssaire (CPU, RAM, Memoire disk)
- Demarage rapide de nos conteneurs
- Plus d'autonomie à vos developpeurs


#                ---- DOCKER ----

 # CHAPITRE I : LANCONS NOTRE CONTENEUR EN LOCAL 

### Qu'est-ce qu'une Registry
Une registry est un logiciel qui permet de partager des images à d'autres presonnes. C'est un composant majeur dans l'écosystème Docker, car il permet :
- à des développeurs de distribuer des images prêtes à l’emploi et de les versionner avec un système de tags
- à des outils d’intégration en continu de jouer une suite de tests, sans avoir besoin d’autre chose que de Docker ;
- à des systèmes automatisés de déployer ces applications sur vos environnement de développement et de production.

 ### PREMIER CONTENEUR DOCKER

Docker run hello-world; Cette commande va chercher l'image hello-world en passant par differentes étapes:
- Le client Docker contact le demon docker 
- Le demon docker extrait l'image demandé du docker hub s'il est disponible en local(dans le cas contrait, il va la recuperer sur la registry Docker officielle.)
- le demon docker crée un nouveau conteneur à partir de l'image qui execute l'executable qui produit une sortie.
- Le demon docker diffuse la sortie sur le client Docker, qui l'envoie à votre terminal

   Si l'on souhaite que le conteneur reste allumé jusqu’à l'arrêt du service qu'il contient, il faudra ajouter l’argument --detach (-d).
Celui ci permet de ne pas rester attacher au conteneur, et donc de pouvoir lancer plusieurs conteneurs.


### Demarrer un serveur Nginx avec un conteneur Docker

Pour aller unpeu plus loin, lançons un conteneur qui demare un serveur Nginx en utilisant deux option:
docker run -d -p 8080:80 nginx (docker container run --publish 8000:8080 --detach --name test nginx)

Dans cette commande nous avons utilisé: 
* -d pour detacher le conteneur du processus principal de la console. il nous permet de continuer à utliser ma console pendant que notre conteneur tourne sur un autre processus
* -p pour definir l'utilisation de ports. Dans notre cas nous demandons de de transferer le trafic du port 8080 vers le port 80 du conteneur. Ainsi en nous rendant sur l'adresse http://127.0.0.1:8080, nous aurons la page par defaut de Nginx.

Vous pourriez aussi avoir besoin de "rentrer" dans votre conteneur Docker pour pouvoir y effectuer des actions. Pour cela, vous devez utiliser la commande docker exec -ti ID_RETOURNÉ_LORS_DU_DOCKER_RUN bash. Dans cette commande, l'argument -ti 
permet d'avoir un shell bash pleinement opérationnel. Une fois que vous êtes dans votre conteneur, vous pouvez vous rendre, via la commande cd /usr/share/nginx/html, dans le répertoire où se trouve le fichier index.html, pour modifier son contenu 
et voir le résultat en direct à l'adresse http://127.0.0.1:8080.Vous pourriez aussi avoir besoin de "rentrer" dans votre conteneur Docker pour pouvoir y effectuer des actions. Pour cela, vous devez utiliser la commande docker exec -ti ID_RETOURNÉ_LORS_DU_DOCKER_RUN bash. 
Dans cette commande, l'argument -ti permet d'avoir un shell bash pleinement opérationnel. Une fois que vous êtes dans votre conteneur, vous pouvez vous rendre, via la commande cd /usr/share/nginx/html, dans le répertoire où se trouve le fichier index.html, pour modifier 
son contenu et voir le résultat en direct à l'adresse http://127.0.0.1:8080.

### ARRETER UN CONTENEUR DOCKER

Vu que nous avons créé notre conteneur avec l'option --detach(-d), nous aurons donc sûrement besoin de l'arrêter. pour cela, nous faisons appel à la commande :
     docker stop ID_DOCKER_RUN. 
Cette commande va detruire le conteneur et son contenu.


### RECUPERER UNE IMAGE DE DOCKER hub

docker pull nom_de_l_image

### AFFICHER L'ENSEMBLE des conteneurs existant 

Quand nous créons des conteneurs avec l'option --detach(-d), nous pouvons avir besoin de savoir si les conteneurs sont toujours actifs; Pour cela, on utilise la commande :
     docker ps

Pour voir l'ensemble des images en local sur notre ordinateur : 
     docker images -a 

### COMMENT NETOYER MON SYSTEME

Pour cela deux possibilités s'offrent à nous :
- Suppression manuelle des images
- Laisser docker lui meme faire le ménage en tapant la commande : docker system prune
Cette commande supprime : 
 * l'ensemble des conteneurs Docker qui ne sont pas en status running ;
 * l'ensemble des réseaux créés par Docker qui ne sont pas utilisés par au moins un conteneur ;
 * l'ensemble des images Docker non utilisées ;
 * l'ensemble des caches utilisés pour la création d'images Docker. 


 # CHAPITRE II : CREONS NOTRE PREMIER DOCKERFILE
