import pygame, sys, random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 600))
screen.fill("White")
pygame.display.set_caption("Recer")
WIDHT = 400
HIGHT = 600
SPEED = 5

background = pygame.image.load("lab8\AnimatedStreet.png")

fps = pygame.time.Clock()
FPS = 60

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDHT-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surFace):
        surFace.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed[K_LEFT]: self.rect.move_ip(-5, 0)
        if self.rect.right < 400:
            if pressed[K_RIGHT]: self.rect.move_ip(5, 0)

    def draw(self, surFace):
        surFace.blit(self.image, self.rect)



P1 = Player()
E1 = Enemy()

while True:

    screen.blit(background, (0, 0))

    P1.update()
    E1.move()
     
    #screen.fill("White")
    P1.draw(screen)
    E1.draw(screen)
         
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit()

    fps.tick(FPS)


