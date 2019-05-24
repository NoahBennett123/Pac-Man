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
SCARY = pygame.image.load('scary1.jfif')
SCARY = pygame.transform.scale(SCARY, (400,300))
fort = pygame.image.load('win.jpg')
fort = pygame.transform.scale(fort, (400,300))


gho1 = ghostone()
gho2 = ghosttwo()
gho3 = ghostthree()
gho4 = ghostfour()
gho5 = ghostfive()

is_game_over = False
win = False

def collide_g():
    global screen, is_game_over
    if pac_class.rect.colliderect(gho1.rect) or  pac_class.rect.colliderect(gho2.rect) or  pac_class.rect.colliderect(gho3.rect) or  pac_class.rect.colliderect(gho4.rect) or  pac_class.rect.colliderect(gho5.rect):
        screen = SCARY
        is_game_over = True
        gho1.kill()
        gho2.kill()
        gho3.kill()
        gho4.kill()
        gho5.kill()
        pac_class.kill()

def wins():
    global win, points, is_game_over
    if points == 10:

        win == True









while True:
    DISPLAYSURF.blit(screen,(background_x, background_y))
    x,y = pygame.mouse.get_pos()
    if y > 85 and y < 149 and x >25 and x < 373 and not is_game_over:
        screen = GAME

    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    pac_class.up()
                if event.key==K_DOWN:
                    pac_class.down()
                if event.key==K_LEFT:
                    pac_class.left()
                if event.key==K_RIGHT:
                    pac_class.Right()

    if not is_game_over:
        DISPLAYSURF.blit(pac_class.image,(pac_class.rect.x, pac_class.rect.y))
        DISPLAYSURF.blit(gho1.image,(gho1.rect.x, gho1.rect.y))
        DISPLAYSURF.blit(gho2.image,(gho2.rect.x, gho2.rect.y))
        DISPLAYSURF.blit(gho3.image,(gho3.rect.x, gho3.rect.y))
        DISPLAYSURF.blit(gho4.image,(gho4.rect.x, gho4.rect.y))
        DISPLAYSURF.blit(gho5.image,(gho5.rect.x, gho5.rect.y))
        gho1.g1move()
        gho2.g2move()
        gho3.g3move()
        gho4.g4move()
        gho5.g5move()
        collide_g()
        points = points + 1
        wins()
        if win == True:
            screen = fort


    pygame.display.update()
    fpsClock.tick(FPS)
