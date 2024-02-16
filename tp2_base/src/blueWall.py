import pygame
from  src.wall import Wall
from src.player import Player

class BlueWall(Wall):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('./assets/blue.png')


