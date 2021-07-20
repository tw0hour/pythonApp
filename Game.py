import pygame

from Case import Case
from Players import Player


class Game:

    def __init__(self):
        # JEU A COMMMENCER OU PAS
        self.is_playing = False
        # create player
        self.player = Player()
        self.case1 = Case()

    def update(self, screen,  BackGround):

        # apply boardGame image
        screen.blit(BackGround, (0, 0))

        # apply player image
        screen.blit(self.player.image, self.player.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("close game")
