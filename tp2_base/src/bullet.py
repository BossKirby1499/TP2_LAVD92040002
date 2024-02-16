import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,grab,mvmtX,mvmtY):
        super().__init__()
        self.image = pygame.image.load('./assets/circle-symbol.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.grab = grab
        self.mvmtX = mvmtX
        self.mvmtY = mvmtY

    def onCollided(self,type):
            return False
    def update(self):
         if not self.grab:
            self.rect.y += self.mvmtY
            self.rect.x += self.mvmtX