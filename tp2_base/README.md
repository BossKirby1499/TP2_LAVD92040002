# Moon Tank TP2
ÉTS, LOG725-01, TP2 
Par David Lavigueur

Présenté à Gabriel C. Ullmann

## Le jeu
Cette démonstration contient un exemple de un niveau du jeu moon tank avec toutes les implémentations pour faire fonctionner le jeu.
Le but du jeu est de sortir d'un labyrinthe avec un tank. Des murs vous barrent la route vous barrent la route, mais certains peuvent être brisés
en associant un tir de balle de la couleur correspondante au mur. 

## Instructions
- Installez pygame : `pip install pygame`
- Exécutez le jeu : `python main.py`

## Fonctionnalités déjà implémentées
- 2 entités (Player et Wall)
- Chargement des sprites pour les entités
- Collision
- Mouvement
## Fonctionnalités implémentés lors du TP 2
-  Ajouts des différents murs de couleurs et des balles de fusils
-  Ajout de la capacité à ramasser les balles de couleurs et de les emmagasiner
-  Ajout de la capacité à tirer les balles de couleurs dans la direction du tank
-  Ajout des collisions entre les murs de couleurs et des balles
-  Ajout du mouvement du sprite pour regarder et tourner dans la bonne direction
-  Ajout du sprite de fin et du message indiquant que le jeu est terminé
-  Ajout de la collision pour déterminer de la fin du jeu
-  Ajout des sons lors d'un tir du tank et lors de l'atteinte de la fin du jeu
-  Ajout du bouton permettant de redémarrer le jeu
-  Ajout des boutons de tirs

## Mouvements
- Les flèches UP et DOWN permettent de faire avancer et reculer le Tank
- Les flèches LEFT et RIGHT permettent de faire tourner le Tank de gauche ou droite à 90 degré
Cela à pour but d'imiter les déplacement d'un tank et de faciliter le déplacement

- La touche Z du clavier permet de tirer une balle ROUGE
- La touche X du clavier permet de tirer une balle BLEU
- La touche C du clavier permet de tirer une balle VERTE

## REPO GITHUB 


  

## Sprites
- Tank: https://www.pngkey.com/download/u2q8a9w7t4u2e6r5_tanks-2d-top-down-tank/
- Son de victoire : https://pixabay.com/sound-effects/search/congrats/
- Son coup de fusil : https://www.sound-searcher.com/sound.php?id=8299
- Image de fin: https://cdn.vectorstock.com/i/preview-1x/09/64/finish-flag-background-vector-9800964.jpg
- Les autres sprites sont par Gabriel C. Ullmann, 2017
