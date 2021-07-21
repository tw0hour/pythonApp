import math
from tkinter import messagebox, Tk
import pygame
from Game import Game

pygame.init()

# app name
pygame.display.set_caption("Jeu de plateau")
# window's size
screen = pygame.display.set_mode((869, 900))
# 784

# load home image
background = pygame.image.load('ressources/greyBG.png')
# load boardGame image
boardGame = pygame.image.load('ressources/BoardGame.png')

#   MENU

# button start game
play_button = pygame.transform.scale(pygame.image.load('ressources/button/playButton.png'), (128, 76))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil((screen.get_width() / 2) - (128 / 2))
play_button_rect.y = math.ceil(screen.get_height() / 4 - (76 / 2))

# button quit menu game
quit_button_menu = pygame.transform.scale(pygame.image.load('ressources/button/quitter.png'), (152, 76))
quit_button_menu_rect = quit_button_menu.get_rect()
quit_button_menu_rect.x = math.ceil((screen.get_width() / 2) - (152 / 2))
quit_button_menu_rect.y = math.ceil(screen.get_height() / 2 + screen.get_height() / 4 - (76 / 2))

# button load game
load_button = pygame.transform.scale(pygame.image.load('ressources/button/charger.png'), (164, 76))
load_button_rect = load_button.get_rect()
load_button_rect.x = math.ceil((screen.get_width() / 2) - (164 / 2))
load_button_rect.y = math.ceil(screen.get_height() / 2 - (76 / 2))

# IN GAME

# button quit game
quit_button = pygame.transform.scale(pygame.image.load('ressources/button/quitter.png'), (152, 76))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = math.ceil((screen.get_width() / 2) - (152 / 2) + (screen.get_width() / 4))
quit_button_rect.y = 800

# button save game
save_button = pygame.transform.scale(pygame.image.load('ressources/button/sauvegarder.png'), (208, 76))
save_button_rect = save_button.get_rect()
save_button_rect.x = math.ceil((screen.get_width() / 2) - (208 / 2) - (screen.get_width() / 4))
save_button_rect.y = 800

# button game menu
menu_button = pygame.transform.scale(pygame.image.load('ressources/button/menu.png'), (133, 76))
menu_button_rect = menu_button.get_rect()
menu_button_rect.x = math.ceil((screen.get_width() / 2) - (133 / 2))
menu_button_rect.y = 800

# load game
game = Game()
Tk().wm_withdraw()  # to hide the main window
running = True

while running:

    if game.is_playing:
        # game started
        game.update(screen, boardGame)
        screen.blit(quit_button, quit_button_rect)
        screen.blit(save_button, save_button_rect)
        screen.blit(menu_button, menu_button_rect)

    else:
        # Home screen
        screen.blit(background, (0, 0))
        screen.blit(play_button, play_button_rect)
        screen.blit(quit_button_menu, quit_button_menu_rect)
        screen.blit(load_button, load_button_rect)

    # apply background and change
    pygame.display.flip()

    # event
    for event in pygame.event.get():

        # on press close key
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("close tab menu")
        # end on press close key

        # mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # EVENT MENU
            if play_button_rect.collidepoint(event.pos) & (game.is_playing == False):
                game.is_playing = True

            if quit_button_menu_rect.collidepoint(event.pos) & (game.is_playing == False):

                MsgBox = messagebox.askquestion('Quitter', 'Voulez vous vraiment quittter l\'application ?')
                if MsgBox == "yes":
                    running = False
                    pygame.quit()
                    print("close tab menu")

            if load_button_rect.collidepoint(event.pos) & (game.is_playing == False):
                MsgBox = messagebox.askquestion('Charger', 'Voulez vous charger la derniere partie sauvegarder ?')
                if MsgBox == "yes":
                    game.load()
                    game.is_playing = True

            # EVENT IN GAME
            if save_button_rect.collidepoint(event.pos) & game.is_playing:
                MsgBox = messagebox.askquestion('Sauvegarder', 'Voulez vous sauvegarder et quitter ?')
                if MsgBox == "yes":
                    game.save()
                    game.gameReset()
                    game.is_playing = False

            if menu_button_rect.collidepoint(event.pos) & game.is_playing:
                MsgBox = messagebox.askquestion('Menu', 'Voulez vous sauvegarder avant de retourner au menu ?')
                if MsgBox == "yes":
                    game.save()
                game.gameReset()
                game.is_playing = False

            if quit_button_rect.collidepoint(event.pos) & game.is_playing:
                Tk().wm_withdraw()  # to hide the main window
                MsgBox = messagebox.askquestion('Quitter', 'Voulez vous vraiment quitter ?')
                if MsgBox == "yes":
                    running = False
                    pygame.quit()
                    print("close tab menu")
        # end mouse click

    # end event
