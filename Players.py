import pygame


class Player(pygame.sprite.Sprite):
    # TODO: need to define attribute
    def __init__(self, imgPath):
        super().__init__()
        self.money = 100
        self.point = 100
        self.image = pygame.transform.scale(pygame.image.load(imgPath), (25, 25))
        self.rect = self.image.get_rect()

        # left right
        self.rect.x = 30
        # up down
        self.rect.y = 30
        self.turn = False

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