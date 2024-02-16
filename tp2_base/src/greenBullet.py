import pygame
from src.bullet import Bullet

class GreenBullet(Bullet):
    def __init__(self, x, y, width, height,grab,mvmtX,mvmtY):
       super().__init__(x, y, width, height,grab,mvmtX,mvmtY)
       self.image = pygame.image.load('./assets/green_circle.png')
       self.image = pygame.transform.scale(self.image,(width,height))


