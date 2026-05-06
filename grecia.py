import pygame
pygame.init()

ventana= pygame.display.set_mode((600, 360))

pygame.display.set_caption("PyGame Test")

azul= (5, 94, 117)
blanco= (255, 255, 255)

superficie_1 = pygame.Surface((600, 360))
superficie_1.fill(azul)
superficie_2 = pygame.Surface((40, 200))
superficie_2.fill(blanco)
superficie_3 = pygame.Surface((200, 40))
superficie_3.fill(blanco)
superficie_4 = pygame.Surface((600, 40))
superficie_4.fill(blanco)
superficie_5 = pygame.Surface((600, 40))
superficie_5.fill(blanco)
superficie_6 = pygame.Surface((400, 40))
superficie_6.fill(blanco)
superficie_7 = pygame.Surface((400, 40))
superficie_7.fill(blanco)

ventana.blit(superficie_1, (0, 0))
ventana.blit(superficie_2, (80, 0))
ventana.blit(superficie_3, (0, 80))
ventana.blit(superficie_4, (0, 280))
ventana.blit(superficie_5, (0, 200))
ventana.blit(superficie_6, (200, 120))
ventana.blit(superficie_7, (200, 40))
pygame.display.flip()

while True:
    evento = pygame.event.wait()
    if evento.type == pygame.QUIT:
        pygame.quit()
        exit()