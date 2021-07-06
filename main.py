import pygame

pygame.init()


class Player(pygame.sprite.Sprite):
    # TODO: need to define attribute
    def __init__(self):
        self.money = 100
        self.point = 100
        self.image = pygame.image.load('ressources/2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500


# app name
pygame.display.set_caption("Jeu de plateau")
# window's size
screen = pygame.display.set_mode((1500, 1000))
# load image
background = pygame.image.load('ressources/Razer-H1-Wallpaper-2560x1440_290520.png')
# create player
player = Player()
running = True

while running:

    # set background image
    screen.blit(background, (-500, -200))

    # apply background
    pygame.display.flip()

    # apply player image
    screen.blit(player.image, player.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("close my dude")
