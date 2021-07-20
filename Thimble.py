import pygame
import random

class Thimble:
    def __init__(self):
        self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/pion/2.png'), (70, 70))
        self.thimble2 = pygame.transform.scale(pygame.image.load('ressources/pion/2.png'), (70, 70))

    # lancé des dé
    def launchThimble(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        if d1 == 1:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))
        if d1 == 2:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))
        if d1 == 3:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))
        if d1 == 4:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))
        if d1 == 5:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))
        if d1 == 6:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))

        if d2 == 1:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))
        if d2 == 2:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))
        if d2 == 3:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))
        if d2 == 4:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))
        if d2 == 5:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))
        if d2 == 6:
            self.thimble1 = pygame.transform.scale(pygame.image.load('ressources/'), (70, 70))

        return d1 + d2
    
