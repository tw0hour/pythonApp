import pygame

from Case import Case
from Players import Player


class Game:

    def __init__(self):
        # create player
        self.player = Player()
        self.case1 = Case()
