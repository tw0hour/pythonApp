from initPyGame import *

while running:
    screen.blit(background, (-500, -200))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("close my dude")
