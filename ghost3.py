import pygame, sys, time, random
from pygame.locals import *

ghost3 = pygame.image.load('pghost.png')
ghost3 = pygame.transform.scale(ghost3, (35,35))

class ghostthree(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = 30
        self.y = 30
        self.image = ghost2
        self.rect = pygame.Rect(self.x,self.y,35,25)

    def g2move(self):
        num3 = random.randint(1,4)
        if num3 == 1:
            self.x = self.x + 25
            if self.rect.x >= 400:
                self.rect.x = self.rect.x - 25
        if num3 == 2:
            self.x = self.x - 25
            if self.rect.x <= 0:
                self.rect.x = self.rect.x + 25
        if num3 == 3:
            self.y = self.y + 25
            if self.rect.y >= 300:
                self.rect.y = self.rect.y - 25
        if num3 == 4:
            self.y = self.y - 25
            if self.rect.y <= 0:
                self.rect.y = self.rect.y + 25
