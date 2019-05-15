import pygame, sys, time, random
from pygame.locals import *

ghost4 = pygame.image.load('rghost.png')
ghost4 = pygame.transform.scale(ghost4, (35,35))

class ghostfour(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = 40
        self.y = 40
        self.image = ghost2
        self.rect = pygame.Rect(self.x,self.y,35,25)

    def g2move(self):
        num4 = random.randint(1,4)
        if num4 == 1:
            self.x = self.x + 25
            if self.rect.x >= 400:
                self.rect.x = self.rect.x - 25
        if num4 == 2:
            self.x = self.x - 25
            if self.rect.x <= 0:
                self.rect.x = self.rect.x + 25
        if num4 == 3:
            self.y = self.y + 25
            if self.rect.y >= 300:
                self.rect.y = self.rect.y - 25
        if num4 == 4:
            self.y = self.y - 25
            if self.rect.y <= 0:
                self.rect.y = self.rect.y + 25
