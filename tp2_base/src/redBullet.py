import pygame
from src.bullet import Bullet

class RedBullet(Bullet):
    def __init__(self, x, y, width, height,grab,mvmtX,mvmtY):
       super().__init__(x, y, width, height,grab,mvmtX,mvmtY)
       self.image = pygame.image.load('./assets/Red_Circle.svg')
       self.image = pygame.transform.scale(self.image,(width,height))


