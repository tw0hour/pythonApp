import json
import random
import pygame

from Case import Case
from Event import Event
from Players import Player
from Thimble import Thimble


class Game:
    def __init__(self,tab):
        # JEU A COMMMENCER OU PAS
        self.is_playing = False
        self.thimble1 = Thimble()
        self.thimble2 = Thimble()
        self.events = self.getEvents()
        self.cases = self.initializeCases(tab)
        # create player
        self.players = self.initialzePlayers()

    def run(self, screen, tab):

        self.printBoard(screen)
        for i in range(4) :
            screen.blit(self.players[i].image, self.players[i].rect)


    def find_in_list_of_list(self, mylist, pos):
        for sub_list in mylist:
            if pos in sub_list:
                return (mylist.index(sub_list), sub_list.index(pos))
        raise ValueError("'{pos}' is not in list".format(pos=pos))

    def knownCase(self, cases, x, y):
        for case in cases:
            if case.x == x and case.y == y:
                return True
        return False

    def notVisitedCase(self, tab, cases, pos):

        if pos[0] - 1 >= 0 and tab[pos[0]-1][pos[1]] != 0 and not self.knownCase(cases, pos[0] - 1, pos[1]):
            pos[0] -= 1
            return True
        if pos[1] - 1 >= 0 and tab[pos[0]][pos[1]-1] != 0 and not self.knownCase(cases, pos[0], pos[1] - 1):
            pos[1] -= 1
            return True
        if pos[0] + 1 < len(tab) and tab[pos[0]+1][pos[1]] != 0 and not self.knownCase(cases, pos[0] + 1, pos[1]):
            pos[0] += 1
            return True
        if pos[1] + 1 < len(tab[0]) and tab[pos[0]][pos[1]+1] != 0 and not self.knownCase(cases, pos[0], pos[1] + 1):
            pos[1] += 1
            return True

        return False

    def initializeCases(self, tab):
        cases = []
        moneyEvents = [x for x in self.getEvents() if x.target == "money"]
        moveEvents = [x for x in self.getEvents() if x.target == "move"]

        actual = list(self.find_in_list_of_list(tab, -1))
        cases.append(Case(actual[0], actual[1], None))

        while self.notVisitedCase(tab, cases, actual):
            i, j = actual[0], actual[1]
            if tab[i][j] == 2:
                if len(moveEvents) > 0:
                    cases.append(Case(i, j, moveEvents.pop()))
                else:
                    tab[i][j] = 1

            if tab[i][j] == 3:
                if len(moneyEvents) > 0:
                    cases.append(Case(i, j, moneyEvents.pop()))
                else:
                    tab[i][j] = 1

            if tab[i][j] == 1 or tab[i][j] == -1 or tab[i][j] == -2:
                cases.append(Case(i, j, None))

        return cases

    def initialzePlayers(self):
        posX = self.cases[0].y * (70 + 5) + 30
        posY = self.cases[0].x * (70 + 5) + 30
        players = []
        players.append(Player("ressources/pion/pion0.png", posX, posY))
        players.append(Player("ressources/pion/pion1.png", posX + 25, posY))
        players.append(Player("ressources/pion/pion2.png", posX, posY + 25))
        players.append(Player("ressources/pion/pion3.png", posX +25 , posY + 25))
        return players

    def getEvents(self):
        with open("ressources/events.json") as file:
            events = []
            data = json.load(file)
            dataEvents = data["events"]

            for event in dataEvents:
                events.append(Event(event["id"], event["target"], event["effect"]))

            return events

    def printBoard(self, screen):

        pygame.draw.rect(screen, (0, 0, 0), (self.cases[0].y * (70 + 5) + 30, self.cases[0].x * (70 + 5) + 30, 70, 70))
        pygame.draw.rect(screen, (0, 0, 0), (self.cases[-1].y * (70 + 5) + 30, self.cases[-1].x * (70 + 5) + 30, 70, 70))

        for i in self.cases[1:-1]:
            posX = i.x * (70 + 5) + 30
            posY = i.y * (70 + 5) + 30
            # normal case
            if i.event is None:
                pygame.draw.rect(screen, (66, 135, 245), (posY, posX, 70, 70))

            # move event case
            elif i.event.target == "move":
                pygame.draw.rect(screen, (255, 36, 65), (posY, posX, 70, 70))

            # money event case
            elif i.event.target == "money":
                pygame.draw.rect(screen, (255, 189, 36), (posY, posX, 70, 70))

    # def update(self, screen, BackGround):
    #
    #     # apply boardGame image
    #     screen.blit(BackGround, (0, 0))
    #
    #     # apply player image
    #     screen.blit(self.player1.image, self.player1.rect)

    def whoIsFirst(self):
        first = random.randint(0, 3)
        print("whoIsFist :", first)

        self.players[first].turn = True;

        print("Joueur", first, "commence !")

    def switchTurn(self):
        if self.players[0].turn == True:
            self.players[0].turn = False
            self.players[1].turn = True
            print("Au tour du Joueur 2 de jouer !")
            return

        if self.players[1].turn == True:
            self.players[1].turn = False
            self.players[2].turn = True
            print("Au tour du Joueur 3 de jouer !")
            return

        if self.players[2].turn == True:
            self.players[2].turn = False
            self.players[3].turn = True
            print("Au tour du Joueur 4 de jouer !")
            return

        if self.players[3].turn == True:
            self.players[3].turn = False
            self.players[0].turn = True
            print("Au tour du Joueur 1 de jouer !")
            return

    def save(self):
        gameProps = [
            self.players[0].turn,
            self.players[0].money,
            self.players[0].point,
            self.players[0].rect.x,
            self.players[0].rect.y,

            self.players[1].turn,
            self.players[1].money,
            self.players[1].point,
            self.players[1].rect.x,
            self.players[1].rect.y,

            self.players[2].turn,
            self.players[2].money,
            self.players[2].point,
            self.players[2].rect.x,
            self.players[2].rect.y,

            self.players[3].turn,
            self.players[3].money,
            self.players[3].point,
            self.players[3].rect.x,
            self.players[3].rect.y,
        ]
        saveJson = json.dumps(gameProps)

        with open("ressources/backup/backup.json", "w") as backupFile:
            backupFile.write(saveJson)

    def load(self):
        with open("ressources/backup/backup.json") as backupFile:
            data = json.load(backupFile)
            self.players = []

            self.players[0].turn = data[0]
            self.players[0].money = data[1]
            self.players[0].point = data[2]
            self.players[0].rect.x = data[3]
            self.players[0].rect.y = data[4]

            self.players[1].turn = data[5]
            self.players[1].money = data[6]
            self.players[1].point = data[7]
            self.players[1].rect.x = data[8]
            self.players[1].rect.y = data[9]

            self.players[2].turn = data[10]
            self.players[2].money = data[11]
            self.players[2].point = data[12]
            self.players[2].rect.x = data[13]
            self.players[2].rect.y = data[14]

            self.players[3].turn = data[15]
            self.players[3].money = data[16]
            self.players[3].point = data[17]
            self.players[3].rect.x = data[18]
            self.players[3].rect.y = data[19]

        return

    def gameReset(self):
        self.is_playing = False
        self.players[0].playerReset()
        self.players[1].playerReset()
        self.players[2].playerReset()
        self.players[3].playerReset()

        return

    def movePawn(self,nb):
        if self.players[0].turn:
            self.players[0].move(self.cases[nb].y * (70 + 5) + 30, self.cases[nb].x * (70 + 5) + 30)
            return
        if self.players[1].turn:
            self.players[1].move(self.cases[nb].y * (70 + 5) + 30 + 25, self.cases[nb].x * (70 + 5) + 30)
            return
        if self.players[2].turn:
            self.players[2].move(self.cases[nb].y * (70 + 5) + 30, self.cases[nb].x * (70 + 5) + 30 + 25)
            return
        if self.players[3].turn:
            self.players[3].move(self.cases[nb].y * (70 + 5) + 30 + 25, self.cases[nb].x * (70 + 5) + 30 + 25)
            return
