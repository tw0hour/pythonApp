import pygame
import random


class Thimble:
    def __init__(self):
        self.thimbleImg = pygame.transform.scale(pygame.image.load('ressources/de/de1.png'), (100, 100))

    # Lance le dé
    def launchThimble(self):
        d = random.randint(1, 6)

        if d == 1:
            self.thimbleImg = pygame.transform.scale(pygame.image.load('ressources/de/de1.png'), (100, 100))
        if d == 2:
            self.thimbleImg = pygame.transform.scale(pygame.image.load('ressources/de/de2.png'), (100, 100))
        if d == 3:
            self.thimbleImg = pygame.transform.scale(pygame.image.load('ressources/de/de3.png'), (100, 100))
        if d == 4:
            self.thimbleImg = pygame.transform.scale(pygame.image.load('ressources/de/de4.png'), (100, 100))
        if d == 5:
            self.thimbleImg = pygame.transform.scale(pygame.image.load('ressources/de/de5.png'), (100, 100))
        if d == 6:
            self.thimbleImg = pygame.transform.scale(pygame.image.load('ressources/de/de6.png'), (100, 100))

        print("Valeur du dé :", d)

        return d

    # Lance les dés et retoune la somme deux deux
    def sumThimble(self, thimble):
        print("Somme des deux dé :", self.launchThimble() + thimble.launchThimble())
        return self.launchThimble() + thimble.launchThimble()
