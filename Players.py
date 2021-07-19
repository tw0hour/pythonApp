import random

import pygame


class Player(pygame.sprite.Sprite):
    # TODO: need to define attribute
    def __init__(self):
        super().__init__()
        self.money = 100
        self.point = 100
        self.image = pygame.image.load('ressources/2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500

    def gainMoney(self, money):
        self.money += money

    def loseMoney(self, money):
        if self.money < money:
            self.money = 0

        self.money -= money

    def gainPoint(self, point):
        self.point += point

    def losePoint(self, point):
        if self.point < point:
            self.point = 0

        self.point -= point

    # lancé du dé
    def launchThimble(self):
        d = random.randint(1,6)
        return d
