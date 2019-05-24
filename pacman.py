import pygame, sys, time, random
from pygame.locals import *

p_pic = pygame.image.load('pac.pic.png')

class pac_class(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = p_pic
        self.image = pygame.transform.scale(p_pic, (25,25))
        self.x = 300
        self.y = 300
        self.rect = pygame.Rect(self.x, self.y, 25, 25)

    def up(self):
        self.rect.y = self.rect.y - 25
        if self.rect.y <= 0:
            self.rect.y = self.rect.y + 25

    def left(self):
        self.rect.x = self.rect.x - 25
        if self.rect.x <= 0:
            self.rect.x = self.rect.x + 25

    def Right(self):
        self.rect.x = self.rect.x + 25
        if self.rect.x >= 400:
            self.rect.x = self.rect.x - 25

    def down(self):
        self.rect.y = self.rect.y + 25
        if self.rect.y >= 300:
            self.rect.y = self.rect.y - 25
