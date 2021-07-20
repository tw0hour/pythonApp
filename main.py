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
    # end event
