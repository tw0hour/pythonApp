import pygame.sprite

from Event import Event


class Case(pygame.sprite.Sprite):
    def __init__(self, x, y, event):
        self.x = x
        self.y = y
        self.event = event
