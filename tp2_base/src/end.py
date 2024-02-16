import pygame
from  src.wall import Wall
from src.player import Player

class End(Wall):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('./assets/termine.jpg')
        self.image = pygame.transform.scale(self.image,(width,height))



