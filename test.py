import pygame
pygame.init()

ventana= pygame.display.set_mode((400, 400))

pygame.display.set_caption("PyGame Test")

rojo= (255, 0, 0)
verde= (0, 255, 0)
azul= (0, 0, 255)
amarillo= (255, 255, 0)
blanco= (255, 255, 255)

superficie_1 = pygame.Surface((200, 200))
superficie_1.fill(rojo)
superficie_2 = pygame.Surface((200, 200))
superficie_2.fill(verde)
superficie_3 = pygame.Surface((200, 200))
superficie_3.fill(azul)
superficie_4 = pygame.Surface((200, 200))
superficie_4.fill(amarillo)
superficie_5 = pygame.Surface((50, 50))
superficie_5.fill(blanco)

ventana.blit(superficie_1, (0, 0))
ventana.blit(superficie_2, (200, 0))
ventana.blit(superficie_3, (0, 200))
ventana.blit(superficie_4, (200, 200))
ventana.blit(superficie_5, (175, 175))
pygame.display.flip()

while True:
    evento = pygame.event.wait()
    if evento.type == pygame.QUIT:
        pygame.quit()
        exit()