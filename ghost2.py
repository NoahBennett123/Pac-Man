import pygame, sys, time, random
from pygame.locals import *

ghost2 = pygame.image.load('ghost.png')
ghost2 = pygame.transform.scale(ghost2, (35,35))

class ghosttwo(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = 20
        self.y = 20
        self.image = ghost2
        self.rect = pygame.Rect(self.x,self.y,35,25)

    def g2move(self):
        num2 = random.randint(1,4)
        if num2 == 1:
            self.x = self.x + 25
            if self.rect.x >= 400:
                self.rect.x = self.rect.x - 25
        if num2 == 2:
            self.x = self.x - 25
            if self.rect.x <= 0:
                self.rect.x = self.rect.x + 25
        if num2 == 3:
            self.y = self.y + 25
            if self.rect.y >= 300:
                self.rect.y = self.rect.y - 25
        if num2 == 4:
            self.y = self.y - 25
            if self.rect.y <= 0:
                self.rect.y = self.rect.y + 25
