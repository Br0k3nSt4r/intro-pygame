import pygame
pygame.init()

pantalla= pygame.display.set_mode((370, 472))
pygame.display.set_caption("Mario Bros")
negro= (0, 0, 0)
pantalla.fill(negro)

mario= pygame.image.load("intro-pygame/assets/images/mario03.png").convert()
pantalla.blit(mario, (5,5))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()