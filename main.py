from initPyGame import *

running = True

while running:
    # arriere plan image
    screen.blit(background, (-500, -200))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("close my dude")
