import json
import random

from Case import Case
from Players import Player
from Thimble import Thimble


class Game:
    def __init__(self):
        # JEU A COMMMENCER OU PAS
        self.is_playing = False
        # create player
        self.player1 = Player('ressources/pion/1.png')
        self.player2 = Player('ressources/pion/2.png')
        self.player3 = Player('ressources/pion/3.png')
        self.player4 = Player('ressources/pion/4.png')

        self.thimble1 = Thimble()
        self.thimble2 = Thimble()

        self.case1 = Case()

    def update(self, screen, BackGround):

        # apply boardGame image
        screen.blit(BackGround, (0, 0))

        # apply player image
        screen.blit(self.player1.image, self.player1.rect)

    def whoIsFirst(self):
        first = random.randint(1, 4)
        print("whoIsFist :", first)

        if first == 1:
            self.player1.turn = True
        if first == 2:
            self.player2.turn = True
        if first == 3:
            self.player3.turn = True
        if first == 4:
            self.player4.turn = True

        print("Joueur", first, "commence !")

    def switchTurn(self):
        if self.player1.turn == True:
            self.player1.turn = False
            self.player2.turn = True
            print("Au tour du Joueur 2 de jouer !")
            return

        if self.player2.turn == True:
            self.player2.turn = False
            self.player3.turn = True
            print("Au tour du Joueur 3 de jouer !")
            return

        if self.player3.turn == True:
            self.player3.turn = False
            self.player4.turn = True
            print("Au tour du Joueur 4 de jouer !")
            return

        if self.player4.turn == True:
            self.player4.turn = False
            self.player1.turn = True
            print("Au tour du Joueur 1 de jouer !")
            return


    def save(self): #KO  <Object of type function is not JSON serializable>
        saveJson = json.dumps(vars(Game))
        with open("ressources/backup/backup.json", "w") as backupFile:
            backupFile.write(saveJson)