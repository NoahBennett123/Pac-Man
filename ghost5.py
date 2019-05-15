import pygame, sys, time, random
from pygame.locals import *

ghost5 = pygame.image.load('yghost.png')
ghost5 = pygame.transform.scale(ghost5, (35,35))

class ghostfive(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 50
        self.image = ghost2
        self.rect = pygame.Rect(self.x,self.y,35,25)

    def g2move(self):
        num5 = random.randint(1,4)
        if num5 == 1:
            self.x = self.x + 25
            if self.rect.x >= 400:
                self.rect.x = self.rect.x - 25
        if num5 == 2:
            self.x = self.x - 25
            if self.rect.x <= 0:
                self.rect.x = self.rect.x + 25
        if num5 == 3:
            self.y = self.y + 25
            if self.rect.y >= 300:
                self.rect.y = self.rect.y - 25
        if num5 == 4:
            self.y = self.y - 25
            if self.rect.y <= 0:
                self.rect.y = self.rect.y + 25
