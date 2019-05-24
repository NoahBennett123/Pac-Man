import pygame, sys, time, random
from pygame.locals import *

ghost = pygame.image.load('cghost.png')
ghost = pygame.transform.scale(ghost, (35,35))

class ghostone(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 10
        self.image = ghost
        self.rect = pygame.Rect(self.x,self.y,35,25)

    def g1move(self):
        num = random.randint(1,4)
        if num == 1:
            self.rect.x = self.rect.x + 10
            if self.rect.x >= 400:
                self.rect.x = self.rect.x - 10
        if num == 2:
            self.rect.x = self.rect.x - 10
            if self.rect.x <= 0:
                self.rect.x = self.rect.x + 10
        if num == 3:
            self.rect.y = self.rect.y + 10
            if self.rect.y >= 300:
                self.rect.y = self.rect.y - 10
        if num == 4:
            self.rect.y = self.rect.y - 10
            if self.rect.y <= 0:
                self.rect.y = self.rect.y + 10
