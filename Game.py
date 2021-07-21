import json
import random
import pygame

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

        self.case1 = Case(1,1,1)


    def printBoard(self,screen,tab):
        cases = []
        spaceRect = pygame.Rect(0, 0, 100, 100)

        x = 30
        y = 30
        for i in range(len(tab)):
            x = 30
            y += 55
            for j in range(len(tab[i])):
                # spaceRect.topleft = (5 + (x * 8), 5 + (y * 8))
                if tab[i][j] == 1:
                    pygame.draw.rect(screen, (0, 0, 0), (x, y, 50, 50))
                    # cases.append(Case(x,y,0))
                # else:
                #     cases.append(Case())
                x += 55


    def run(self,screen,tab):
        self.printBoard(screen,tab)

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

    def save(self):
        gameProps = [
            self.player1.turn,
            self.player1.money,
            self.player1.point,
            self.player1.rect.x,
            self.player1.rect.y,

            self.player2.turn,
            self.player2.money,
            self.player2.point,
            self.player2.rect.x,
            self.player2.rect.y,

            self.player3.turn,
            self.player3.money,
            self.player3.point,
            self.player3.rect.x,
            self.player3.rect.y,

            self.player4.turn,
            self.player4.money,
            self.player4.point,
            self.player4.rect.x,
            self.player4.rect.y,
        ]
        saveJson = json.dumps(gameProps)

        with open("ressources/backup/backup.json", "w") as backupFile:
            backupFile.write(saveJson)

    def load(self):
        with open("ressources/backup/backup.json") as backupFile:
            data = json.load(backupFile)

            self.player1.turn = data[0]
            self.player1.money = data[1]
            self.player1.point = data[2]
            self.player1.rect.x = data[3]
            self.player1.rect.y = data[4]

            self.player2.turn = data[5]
            self.player2.money = data[6]
            self.player2.point = data[7]
            self.player2.rect.x = data[8]
            self.player2.rect.y = data[9]

            self.player3.turn = data[10]
            self.player3.money = data[11]
            self.player3.point = data[12]
            self.player3.rect.x = data[13]
            self.player3.rect.y = data[14]

            self.player4.turn = data[15]
            self.player4.money = data[16]
            self.player4.point = data[17]
            self.player4.rect.x = data[18]
            self.player4.rect.y = data[19]

        return

    def gameReset(self):
        self.is_playing = False
        self.player1.playerReset()
        self.player2.playerReset()
        self.player3.playerReset()
        self.player4.playerReset()

        return

    # board_rects = [  ( 200,100,250,250, red ), ( 150,75,350,300, green ), ( 100,50,450,350, red ) ]
    # for rect in board_rects:
    #     x_pos, y_pos  = rect[0], rect[1]
    #     width, height = rect[2], rect[3]
    #     colour        = rect[4]
    #     pygame.draw.rect( screen, colour, ( x_pos, y_pos, width, height ), 2 )

    # int the_round(PLAYER *player,int nb_player,int my_round)
    # {
    #     int value;
    #     if(nb_player==2)
    #     {
    #         if(my_round%2==0)value = 0;
    #         else value = 1;
    #     }
    #     else if(nb_player==3)
    #     {
    #         if(my_round%3==0)value = 0;
    #         else if(my_round%3==1)value = 1;
    #         else if(my_round%3==2)value = 2;
    #     }
    #     else if(nb_player==4)
    #     {
    #         if(my_round%4==0)value = 0;
    #         else if(my_round%4==1)value = 1;
    #         else if(my_round%4==2)value = 2;
    #         else if(my_round%4==3)value = 3;
    #     }
    #
    #     return value;
    # }
