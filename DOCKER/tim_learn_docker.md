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


Un dockerfile est un fichier dans lequel on retrouve l'ensemble de la recette decrivant l'image docker dont nous avons besoin pour notre projet

Les étapes à suivre :
- Créer les instructions dans notre Dockerfile
- Créer un fichier .dockerignore 
- Profiter de l'optimisation Docker 
- Lancer le conteneur personalisé à parir de la commande :
docker build -t orc-docker-build .
  * -t permet de donner un nom à l'image docker.
  * Le . à la fin est le repertoire ou se trouve notre dockerfile 
docker run -d -p 2368:2368 ocr-docker-build (Pour lancer notre conteneur)


### En resumé:
Pour créer une image Docker, vous savez utiliser les instructions suivantes :
- FROM qui vous permet de définir l'image source ;
- RUN qui vous permet d’exécuter des commandes dans votre conteneur ;
- ADD qui vous permet d'ajouter des fichiers dans votre conteneur ;
- WORKDIR qui vous permet de définir votre répertoire de travail ;
- EXPOSE qui permet de définir les ports d'écoute par défaut ;
- VOLUME qui permet de définir les volumes utilisables ;
- CMD qui permet de définir la commande par défaut lors de l’exécution de vos conteneurs Docker.




# CHAPITRE III : UTILISER DES IMAGES GRÂCE AU PARTAGE SUR LE DOCKER HUB

Pour partager une image sur DockerHub, il faut d'abord créer un repository sur mon compte  DockerHub
Après avoir créer notre image via la commande "docker build", nous allons la publier sur le DockerHub:

la première commande est: 
docker tag ocr-docker-build:latest YOUR_USERNAME/ocr-docker-build:latest
Celle-ci va créer un lien entre notre image ocr-docker-build:latest créée précédemment et 
l'image que nous voulons envoyer sur le Docker Hub YOUR_USERNAME/ocr-docker-build:latest

Si le conteneur que nous utilisos n'a pas de nom, nous utilisons son id de conteneur, que nous pouvons récupérer en retour de la commande docker build.
➜ docker tag id_du_conteneur openclassrooms/ocr-docker-build:latest

Maintenant envoyons notre image vers le Docker Hub. Pour cela exécutons la commande :
➜ docker push ocr/ocr-docker-build:latest

### TROUVER LES IMAGES SUR LE DOOCKER HUB
Il existe deux types dimages :
- Les images officielles
- Les images personelles

Dans la recherche d'une image, deu possibilités
- La solution du barbu en ligne de commande
- La solution classique avec l'interface web.


#### EN RESUMÉ :
Deux commandes à retenir :
- Docker push qui permet d'envoyer nos images locales sur une registry 
- docker search qui permet de rechercher une image sur notre registry


# CHAPITRE IV : DECOUVRIR RT INSTALLER DOCKER COMPOSE

     Vous avez un nouveau projet de site avec Wordpress. Pour simplifier la gestion de 
l'infrastructure, vous souhaitez déployer l'ensemble des composants dans des conteneurs Docker. 
Pour cela, nous allons avoir besoin de deux conteneurs :
- un conteneur MySQL ;
- un conteneur Wordpress.

Docker Compose va vous permettre d'orchestrer vos conteneurs, et ainsi de simplifier vos déploiements sur 
de multiples environnements. Docker Compose est un outil écrit en Python qui permet de décrire, dans un fichier YAML, 
plusieurs conteneurs comme un ensemble de services.

### Installation de Docker Compose
Si vous avez utilisé Docker for Mac ou Docker for Windows, vous avez déjà la dernière version de Docker Compose installée dans votre système.
Sur un poste Linux, cela ne sera pas le cas. Vous devez donc le télécharger puis l'installer avec cette ligne de commande (un peu longue, oui !) :
     sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose && sudo chmod +x /usr/bin/docker-compose

Pour verifier la version de docker composer : docker-compose --version

### Decouvrons ensemble le CLI de Docker compose
Pour utiliser le CLI (Command Line Interface) de Docker Compose, nous avons besoin d'un fichier docker-compose.yml que nous allons créer dans le prochain chapitre ! 
Mais avant de le créer, nous allons commencer par découvrir ensemble l'interface en ligne de commande (CLI) qui nous permet d'utiliser le fichier docker-compose.yml.

#### Le CLI de Docker Compose et celui de Docker sont très proches. 
Par exemple, si vous souhaitez récupérer l'ensemble des images décrites dans votre fichier docker-compose.yml et les télécharger depuis le Docker Hub, 
vous devez faire un docker-compose pull. Du côté de Docker, la commande serait un docker pull.

#### NB: 
   Le fait que les deux interfaces en lignes de commandes soit très similaires nous évite d'apprendre un nouveau CLI. Si vous connaissez celui de Docker, 
vous savez globalement utiliser celui de Docker Compose !
Cependant, nous allons quand même voir ensemble les principales commandes que vous pourriez avoir besoin d'utiliser et de connaître pour votre utilisation de Docker Compose.

#### Demarer Une Stack Docker Compose 

Si vous souhaitez lancer la création de l'ensemble des conteneurs, vous devez lancer la commande docker-compose up (pour rappel, vous faites un docker run pour lancer un seul conteneur). 
Vous pouvez ajouter l’argument -d pour faire tourner les conteneurs en tâche de fond.

#### NB: 
   Une "Stack" est un ensemble de conteneur docker lancés via un seul et unique fichier Docker Compose 

#### Verifier l'Etat d'un Stack Docker Compose

Après avoir démarré une stack Docker Compose, vous aurez certainement besoin de voir si l'ensemble des conteneurs sont bien dans un état fonctionnel, et prêts à rendre un service.
Pour cela, vous allez utiliser la commande docker-compose ps qui vous affichera le retour suivant :
ADD CONTENT 

#### Voir les logs d'une Stack Docker Compose

Votre stack Docker Compose est maintenant fonctionnelle, et l'ensemble des services répondent bien ; mais vous pourriez avoir besoin de voir les logs de vos conteneurs. 
Pour cela, vous devez utiliser la commande :
     docker-compose logs -f --tail 5.
Celle-ci permet de voir l'ensemble des logs sur les différents conteneurs de façon continue, tout en limitant l'affichage aux 5 premières lignes.
Ainsi, si nos conteneurs fonctionnent depuis longtemps, nous n'aurons pas à attendre plusieurs secondes, ni voir de nombreux logs qui ne nous intéressent pas.

#### Arrêter une stack Docker Compose
Si vous souhaitez arrêter une stack Docker Compose, vous devez utiliser la commande : 
     docker-compose stop. 
Cependant, Celle-ci ne supprimera pas les différentes ressources créées par votre stack.
Ainsi, si vous lancez à nouveau un "docker-compose up -d", l'ensemble de votre stack sera tout de suite à nouveau fonctionnelle.
Si vous souhaitez supprimer l'ensemble de la stack Docker Compose, vous devez utiliser la commande "docker-compose down" qui détruira l'ensemble des ressources créées.

#### Valider une stack Docker Compose
Lors de l'écriture d'un fichier docker-compose, nous ne sommes pas à l’abri d'une erreur. Pour éviter au maximum cela, vous devez utiliser la commande : 
     docker-compose config qui vous permettra de valider la syntaxe de votre fichier, ainsi d'être certain de son bon fonctionnement.
Si nous créons une erreur dans notre stack, en remplaçant "image" par "images", par exemple, nous aurons le résultat suivant :
➜ docker-compose config
ERROR: The Compose file './docker-compose.yml' is invalid because:
Unsupported config option for services.db: 'images'

### En Resumé

Vous connaissez maintenant les commandes principales pour utiliser une stack Docker Compose. Voici les commandes les plus importantes :
docker-compose up -d vous permettra de démarrer l'ensemble des conteneurs en arrière-plan ;
docker-compose ps vous permettra de voir le status de l'ensemble de votre stack ;
docker-compose logs -f --tail 5 vous permettra d'afficher les logs de votre stack ;
docker-compose stop vous permettra d'arrêter l'ensemble des services d'une stack ;
docker-compose down vous permettra de détruire l'ensemble des ressources d'une stack ;
docker-compose config vous permettra de valider la syntaxe de votre fichier docker-compose.yml.
Mais passons sans plus attendre à un exemple concret ! Et créons notre première stack Docker Compose !


# CHAPITRE V : CREONS NOTRE FICHIER DOCKER-COMPOSE POUR ORCHESTRER NOS CONTENEURS

### Créons notre fichier docker-compose.yml

Nous avons vu dans le chapitre précédent comment utiliser l'interface en ligne de commande de Docker Compose ; 
vous allez maintenant apprendre à créer un fichier docker-compose.yml.

Pour rappel, nous avons un nouveau projet de site avec Wordpress, et nous souhaitons simplifier la gestion de l'infrastructure. 
Nous devons maintenant réaliser un déploiement en production, où l'ensemble des composants sont dans des conteneurs Docker. 
Pour cela, vous allez avoir besoin de plusieurs composants :
- une base de données MySQL ;
- le système de fichiers Wordpress.

### Décrivons notre premier service

#### Definissons laversion de docker Compose
Un fichier docker-compose.yml commence toujours par les informations suivantes:
     version: '3'
L'argument version permet de spécifier à Docker Compose quelle version on souhaite utiliser. Ici nous utilisons la plus utilisée qui la version 3.

#### Déclarons le premier service et son image

Nous allons maintenant déclarer notre premier service, et donc créer notre stack Wordpress!
L'ensemble des conteneurs qui doivent être créés doivent être définis sous l'argument services. Chaque conteneur commence avec un nom qui lui est propre ; dans notre cas, notre premier conteneur se nommera db.

Puis, nous devons decrire notre conteneur; 

#### Definissons le volume pour faire persister vos données 
