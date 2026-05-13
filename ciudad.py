import pygame
pygame.init()

ventana= pygame.display.set_mode((600, 400))

pygame.display.set_caption("ciudad")

cielo= (75, 139, 225)
cesped= (43, 177, 57)
sol= (255, 255, 0)
nube= (255, 255, 255)
edificio= (81, 81, 82)
edificio2= (91, 91, 92)
luz= (236, 240, 176)
rueda= (184, 161, 255)
fortuna= (255, 158, 255)

#cielo/fondo
superficie_1 = pygame.Surface((600, 400))
superficie_1.fill(cielo)
superficie_1.fill(cesped, rect=pygame.Rect(0, 300, 600, 100))
superficie_1.fill(sol, rect=pygame.Rect(500, 50, 75, 75))
superficie_1.fill(nube, rect=pygame.Rect(100, 50, 100, 50))
superficie_1.fill(nube, rect=pygame.Rect(150, 25, 100, 50))
superficie_1.fill(nube, rect=pygame.Rect(200, 50, 100, 50))

#el unico edificio
superficie_2 = pygame.Surface((125, 300))
superficie_2.fill(edificio)
superficie_2.fill(luz, rect=pygame.Rect(20, 25, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(50, 25, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(80, 25, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(20, 55, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(50, 55, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(80, 55, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(20, 85, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(50, 85, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(80, 85, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(20, 115, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(50, 115, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(80, 115, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(20, 145, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(50, 145, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(80, 145, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(20, 175, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(50, 175, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(80, 175, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(20, 205, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(50, 205, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(80, 205, 25, 25))
superficie_2.fill(luz, rect=pygame.Rect(35, 245, 25, 50))
superficie_2.fill(luz, rect=pygame.Rect(65, 245, 25, 50))

#rueda de la fortuna
superficie_3 = pygame.Surface((150, 150))
superficie_3.fill(rueda)
superficie_3.fill(cielo, rect=pygame.Rect(12.5, 12.5, 125, 125))
superficie_3.fill(rueda, rect=pygame.Rect(70, 0, 10, 150))
superficie_3.fill(rueda, rect=pygame.Rect(0, 70, 150, 10))
pygame.draw.polygon(superficie_1, fortuna, [(300, 350), (450, 350), (375, 275)])


ventana.blit(superficie_1, (0, 0))
pygame.display.flip()
ventana.blit(superficie_2, (0, 100))
pygame.display.flip()
ventana.blit(superficie_3, (300, 150))
pygame.display.flip()


while True:
    evento = pygame.event.wait()
    if evento.type == pygame.QUIT:
        pygame.quit()
        exit()
