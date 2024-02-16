import pygame
from src.redBullet import RedBullet
from src.blueBullet import BlueBullet
from src.greenBullet import GreenBullet
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/tank.png')
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.speed = 6
        self.angle = 0
        self.previousAngle = 0 
        self.redBullets = 0
        self.greenBullets = 0
        self.blueBullets = 0

    def addBullet(self,bullet):
        if isinstance(bullet,RedBullet):
            self.redBullets += 1
        elif isinstance(bullet,BlueBullet):
            self.blueBullets += 1

        elif isinstance(bullet,GreenBullet):
            self.greenBullets += 1
            
    def createBullet(self,game,bulletType):
        bullet = None

        res = self.bulletSpawn()
        x,y = res
        posX = self.rect.x +x
        posY = self.rect.y +y
        print(str(posX))
        print(str(posY))

        if bulletType == 0:
            bullet = RedBullet(posX,posY,20,20,False,x,y)
            self.redBullets -= 1
            print(str(self.redBullets))
        elif bulletType == 1:
            bullet = BlueBullet(posX,posY,20,20,False,x,y)
            self.blueBullets -= 1
        elif bulletType == 2:
            bullet = GreenBullet(posX,posY,20,20,False,x,y)
            self.greenBullets -= 1

        game.newBullet(bullet)
        
    #Permet de savoir l'endroit vers lequel les balles doivent se diriger en fonction de l'angle du tank 
    def bulletSpawn(self):
        x=0
        y=0
        speed = 10
        if self.angle == 0 or self.angle % 360 ==  0:
            x = speed
        elif self.angle % 360 == 180:
            x = -speed
        elif self.previousAngle == 0 or self.previousAngle % 360 == 0:
            if self.previousAngle > self.angle: 
                y= speed
            else:
                y = -speed
        else:
             if self.previousAngle > self.angle: 
                y= -speed
             else:
                y = speed
        
        return x,y
  

    def update(self, game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.previousAngle = self.angle
            self.angle += 90
            self.image = pygame.transform.rotate(self.image,90)
            pygame.event.wait(140)
        if keys[pygame.K_RIGHT]:
            self.previousAngle = self.angle
            self.angle -= 90
            self.image = pygame.transform.rotate(self.image,-90)
            pygame.event.wait(140)
        if keys[pygame.K_UP]:
            if (self.angle % 180) != 0:
                self.rect.y -= self.speed
            else:
                self.rect.x -= self.speed
        if keys[pygame.K_DOWN]:
            if (self.angle % 180) != 0:
                self.rect.y += self.speed
            else:
                self.rect.x += self.speed
        if keys[pygame.K_z]:
            if self.redBullets > 0:
                self.createBullet(game,0)
        if keys[pygame.K_x]:
            if self.blueBullets > 0:
                self.createBullet(game,1)
        if keys[pygame.K_c]:
            if self.greenBullets > 0:
                self.createBullet(game,2)

