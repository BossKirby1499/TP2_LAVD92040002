import pygame
import sys
from src.player import Player
from src.wall import Wall
from src.redWall import RedWall
from src.blueWall import BlueWall
from src.redBullet import RedBullet
from src.blueBullet import BlueBullet
from src.greenBullet import GreenBullet
from src.greenWall import GreenWall
from src.end import End

pygame.init()
pygame.mixer.init()


# Define colors
BG_COLOR = (153, 178, 178)

# Initialize Pygame
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


class Game():
    def __init__(self):
        
        # Create entities
        self.end = False     

        self.player = Player()
        redbullet = RedBullet(250, 200, 20, 20,True,0,0)
        bluebullet = BlueBullet(650, 50, 20, 20,True,0,0)
        greenbullet = GreenBullet(400, 450, 20, 20,True,0,0)

        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.finishLine = pygame.sprite.Group()
        wall1 = Wall(500, 150, 50, 200)
        wall2 = Wall(250, 50, 100, 50)
        wall3 = RedWall(350, 50, 100, 50)
        blueWall = BlueWall(350, 250, 100, 50)
        wall4 = Wall(150, 50, 50, 200)
        wall5 = Wall(150, 250, 50, 200)
        wall6 = Wall(250, 250, 50, 200)
        wall7 = Wall(150, -50, 50, 200)
        wall8 = Wall(50, 250, 50, 200)
        wall9 = Wall(-50, 250, 50, 200)
        wall10 = Wall(600, 150, 50, 200)
        wall11 = Wall(700, 150, 50, 200)
        wall12 = Wall(500, 250, 50, 200)
        wall13 = Wall(500, 350, 50, 200)
        wall14 = Wall(500, 450, 50, 200)
        wall15 = Wall(500, 550, 50, 200)
        wall16 = Wall(500, 650, 50, 200)
        wall17 = Wall(250, 350, 50, 200)
        wall18 = Wall(250, 550, 50, 200)
        greenWall = GreenWall(250,450,50,200)
        finish = End(50,450,100,100)



        self.walls.add(wall1, wall2,wall3,blueWall,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16
                ,wall17,wall18,greenWall)
        self.bullets.add(redbullet,bluebullet,greenbullet)
        self.finishLine.add(finish)

    def update(self):
        # before player update
        previous_x = self.player.rect.x
        previous_y = self.player.rect.y

        # player update 
        self.player.update(self)
        
        # keep in bound min
        if (self.player.rect.x < 0 or self.player.rect.y < 0) :
            self.player.rect.x = previous_x
            self.player.rect.y = previous_y
        # keep in bound max
        if self.player.rect.x > 700 or self.player.rect.y > 500:
            self.player.rect.x = previous_x
            self.player.rect.y = previous_y

        # check for collisions between player and walls
        wall_collisions = pygame.sprite.spritecollide(self.player, self.walls, False)
        for wall_collision in wall_collisions:

            # fall back to previous position
            self.player.rect.x = previous_x
            self.player.rect.y = previous_y            
            break

        for bullet in self.bullets:
            wall_bullet_collisions = pygame.sprite.spritecollide(bullet, self.walls, False)
            for wall_bullet_collision in wall_bullet_collisions:
                if isinstance(wall_bullet_collision,RedWall) and isinstance(bullet,RedBullet):
                    wall_bullet_collision.kill()

                
                if isinstance(wall_bullet_collision,BlueWall) and isinstance(bullet,BlueBullet):
                        wall_bullet_collision.kill()
                
                if isinstance(wall_bullet_collision,GreenWall) and isinstance(bullet,GreenBullet):
                        wall_bullet_collision.kill()
        
        end_player_collisions = pygame.sprite.spritecollide(self.player, self.finishLine, False)
        for i in end_player_collisions:
            if not self.end:
                sound = pygame.mixer.Sound("assets/fanfare.mp3")
                sound.play()                
                self.end= True
    
            
        
        bullet_collisions = pygame.sprite.spritecollide(self.player, self.bullets, False)
        for bullet_collision in bullet_collisions:
                if bullet_collision.grab:
                    self.player.addBullet(bullet_collision)
                    bullet_collision.kill()
        for bullet in self.bullets:
            bullet.update()
        

    def newBullet(self, bullet):   
        self.bullets.add(bullet)
        sound = pygame.mixer.Sound("assets/tank firing.mp3")
        sound.play()

game = Game()
# Main game loop

def main():
    playing = True
    while playing:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        game.update()

        screen.fill(BG_COLOR)

        screen.blit(game.player.image, (game.player.rect.x, game.player.rect.y))

        game.walls.draw(screen)
        game.bullets.draw(screen)
        game.finishLine.draw(screen)

        if game.end:
            blanc = (255, 255, 255)
            rouge = (255, 0, 0)

            X = 800
            Y = 600
                        
            font = pygame.font.Font('freesansbold.ttf', 32)
            
            text = font.render('Terminé!', True, rouge, blanc)
            
            textRect = text.get_rect()
            
            # set the center of the rectangular object.
            textRect.center = (X // 2, Y // 2)
            screen.blit(text, textRect)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
             game.__init__()

        pygame.display.flip()
        clock.tick(30)

main()
pygame.quit()
sys.exit()

