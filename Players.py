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