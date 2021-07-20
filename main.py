import pygame
from Game import Game
from Event import Event

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
play_button = pygame.transform.scale(pygame.image.load('ressources/buton/play_buton.png'), (199, 132))
play_button_rect = play_button.get_rect()
play_button_rect.x = 400
play_button_rect.y = 400

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
    # end event
