import pygame
import math

pygame.init()

# Définir des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Définir les dimensions de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Créer la fenêtre de jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotation de sprite")

# Charger l'image de sprite
sprite_image = pygame.image.load("icon.svg")  # Remplacez "sprite.png" par le chemin de votre propre image

# Obtenir le rectangle de l'image
sprite_rect = sprite_image.get_rect()

# Position initiale du sprite
sprite_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Angle initial du sprite
angle = 0

# Vitesse de rotation
rotation_speed = 2

# Variables de contrôle de rotation
rotating_left = False
rotating_right = False
rotated_once = False

# Boucle principale du jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rotating_left = True
            elif event.key == pygame.K_RIGHT:
                rotating_right = True

    # Rotation du sprite
    if rotating_left:
        angle += rotation_speed
        if angle >= 360:
            angle = 0
            rotating_left = False
            rotated_once = True
    elif rotating_right:
        angle -= rotation_speed
        if angle <= -360:
            angle = 0
            rotating_right = False
            rotated_once = True

    # Si le sprite a effectué une rotation complète, arrêtez de le faire tourner
    if rotated_once:
        rotating_left = False
        rotating_right = False

    # Faire pivoter le sprite
    rotated_sprite = pygame.transform.rotate(sprite_image, angle)
    rotated_rect = rotated_sprite.get_rect(center=sprite_rect.center)

    # Effacer l'écran
    screen.fill(WHITE)

    # Dessiner le sprite pivoté
    screen.blit(rotated_sprite, rotated_rect.topleft)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter le nombre d'images par seconde
    pygame.time.Clock().tick(60)

pygame.quit()