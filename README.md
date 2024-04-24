# IA Data Hack : Acoustique groupe 15

Ce repo contient notre participation au [IA Data Hack](https://www.defense.gouv.fr/sga/evenements/hackathon-ia-data-hack), pour le projet acoustique.

Le but de ce projet étant la localisation de personnes à partir d'audios RIRs.

Les membres de ce projet sont:
- Alice CARIOU
- Abel ANDRY
- Matis BRAUN
- Marwane BOUBEUKEUR
- Carla BITAN

## Architecture du projet

Vous pouvez trouver :
- `datasets/` : le dataset sera stocké ici une fois téléchargé
- `indices/` : fichiers utiles
- `research/` : méthodes étudiées avant de choisir la plus adaptée
- `models` : contient les fichiers liés à VGGish
- `acoustic_multichannel.ipynb` : méthode utilisée pour répondre à la problématique du projet
- `room_config.py` : configuration de la salle que nous allons étudier
- `download.ipynb` : script permettant de télécharger les données
- `requirements.txt` : librairies nécessaires au bon fonctionnement du projet

## Préparation de l'environnement

### Téléchargement des librairies nécessaires

Pour installer les librairies manquantes, vous pouvez lancer la commande :  
`pip install -r requirements.txt`

### Récupération des données

Vous pouvez télécharger les données du dataset utilisé ([SoundCam](https://masonlwang.com/soundcam/)) à l'aide du notebook suivant :  
`download.ipynb`  
Ce script permet également de visualiser les données récupérées.

## VGGish multi-channel

C'est la méthode la plus efficace que nous avons trouvée. Le notebook contenant notre code est :
`acoustic_multichannel.ipynb`  
