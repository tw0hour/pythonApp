import random

import pygame


class Player(pygame.sprite.Sprite):
    # TODO: need to define attribute
    def __init__(self):
        super().__init__()
        self.money = 100
        self.point = 100
        self.image = pygame.transform.scale(pygame.image.load('ressources/2.png'), (25, 25))
        self.rect = self.image.get_rect()
        # left right
        self.rect.x = 30
        # up down
        self.rect.y = 30

    # def moveRight(self):
    #     self.rect.x += 20
    #
    # def moveLeft(self):
    #     self.rect.x -= 20
    #
    # def moveUp(self):
    #     self.rect.y -= 20
    #
    # def moveDown(self):
    #     self.rect.y += 20

    def move(self, x, y):
        self.rect.y = y
        self.rect.x = x

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
