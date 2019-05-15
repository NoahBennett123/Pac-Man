import pygame, sys, time
from pygame.locals import *

from pacman import pac_class
from ghost import ghostone
from ghost2 import ghosttwo
from ghost3 import ghostthree
from ghost4 import ghostfour
from ghost5 import ghostfive

FPS = 10
time = 0

pygame.init()

fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption("Man-Pac")

BACKGROUND = pygame.image.load('menu.pic.png')
background_x = 0
background_y = 0





while True:
    DISPLAYSURF.blit(BACKGROUND,(background_x, background_y))
