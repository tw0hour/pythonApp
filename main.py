import pygame
from Game import Game
pygame.init()

# app name
pygame.display.set_caption("Jeu de plateau")
# window's size
screen = pygame.display.set_mode((1500, 1000))
# load image
background = pygame.image.load('ressources/Razer-H1-Wallpaper-2560x1440_290520.png')

# load game
game = Game()

running = True

while running:

    # set background image
    screen.blit(background, (-500, -200))

    # apply player image
    screen.blit(game.player.image, game.player.rect)

    # apply background
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("close my dude")
