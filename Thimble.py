import pygame
import random


class Thimble:
    def __init__(self):
        self.thimbleImg = pygame.transform.scale(pygame.image.load('ressources/de/de1.png'), (100, 100))

    # lancé des dé
    def launchThimble(self):
        d = random.randint(1, 6)

        if d == 1:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/de1'), (100, 100))
        if d == 2:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/de2'), (100, 100))
        if d == 3:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/de3'), (100, 100))
        if d == 4:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/de4'), (100, 100))
        if d == 5:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/de5'), (100, 100))
        if d == 6:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/de6'), (100, 100))

        return d

    def sumThimble(self, thimble):
        return self.launchThimble() + thimble.sumThimble()
