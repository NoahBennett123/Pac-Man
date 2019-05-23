import pygame, sys, time
from pygame.locals import *

from pacman import pac_class
from ghost import ghostone
from ghost2 import ghosttwo
from ghost3 import ghostthree
from ghost4 import ghostfour
from ghost5 import ghostfive

pac_class = pac_class()
points = 0
FPS = 10
time = 0

pygame.init()

fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption("Man-Pac")

BACKGROUND = pygame.image.load('menu.pic.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (400,300))
screen = BACKGROUND
background_x = 0
background_y = 0
GAME = pygame.image.load('game.pic.png')
GAME = pygame.transform.scale(GAME, (400,300))


#gho1 = ghostone(225)
#gho2 = ghosttwo(200)
#gho3 = ghostthree(190)
#gho4 = ghostfour(180)
#gho5 = ghostfive(170)

def collide_g():
    if pac.rect.colliderect(gho.rect or gho1.rect or gho2.rect or gho3.rect or gho4.rect or gho5.rect):
        pygame.quit()
        sys.exit()

def collide_d():
    if pac.rect.colliderect(dot.rect):
        points = points + 100





while True:
    DISPLAYSURF.blit(screen,(background_x, background_y))
    x,y = pygame.mouse.get_pos()
    if y > 85 and y < 149 and x >25 and x < 373:
        screen = GAME
        DISPLAYSURF.blit(pac_class.image,(pac_class.rect.x, pac_class.rect.y))

    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    pacman.up()
                if event.key==K_DOWN:
                    pacman.down()
                if event.key==K_LEFT:
                    pacman.left()
                if event.key==K_RIGHT:
                    pacman.right()

    pygame.display.update()
    fpsClock.tick(FPS)
