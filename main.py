import math
from tkinter import messagebox, Tk

import pygame
from Game import Game

pygame.init()

# app name
pygame.display.set_caption("Jeu de plateau")
# window's size
screen = pygame.display.set_mode((869, 784))

# load home image
background = pygame.image.load('ressources/Razer-H1-Wallpaper-2560x1440_290520.png')

# load boardGame image
boardGame = pygame.image.load('ressources/BoardGame.png')

# button start game
play_button = pygame.transform.scale(pygame.image.load('ressources/button/playButton.png'), (128, 76))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil((screen.get_width() / 2) - (128/2))
play_button_rect.y = math.ceil(screen.get_height() / 4 - (76/2))

# button quit game
quit_button = pygame.transform.scale(pygame.image.load('ressources/button/quitter.png'), (152, 76))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = math.ceil((screen.get_width() / 2) - (152/2))
quit_button_rect.y = math.ceil(screen.get_height() / 2 + screen.get_height() / 4 - (76/2))

# button load game
load_button = pygame.transform.scale(pygame.image.load('ressources/button/charger.png'), (164, 76))
load_button_rect = load_button.get_rect()
load_button_rect.x = math.ceil((screen.get_width() / 2) - (164/2))
load_button_rect.y = math.ceil(screen.get_height() / 2 - (76/2))

# load game
game = Game()
running = True

while running:
    if game.is_playing:
        # game started
        game.update(screen, boardGame)
    else:
        # Home screen
        screen.blit(background, (-850, 0))
        screen.blit(play_button, play_button_rect)
        screen.blit(quit_button, quit_button_rect)
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

        # on key down
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.is_playing = True
            if event.key == pygame.K_LEFT:
                game.is_playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # mouse click
            if play_button_rect.collidepoint(event.pos):
                game.is_playing = True
            if quit_button_rect.collidepoint(event.pos):
                running = False
                pygame.quit()
                print("close tab menu")
            if load_button_rect.collidepoint(event.pos):
                Tk().wm_withdraw()  # to hide the main window
                messagebox.showinfo('ça fais rien tolololol', 'okayyyyyyy?????')
    # end event
