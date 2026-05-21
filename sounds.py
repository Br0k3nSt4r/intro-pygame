import pygame
import sys

pygame.init()
pygame.mixer.init()

blanco= (255, 255, 255)

pantalla= pygame.display.set_mode((400, 400))
pantalla.fill(blanco)
pygame.display.set_caption("Sonidos en PyGame")

continuar = True

Silbato = pygame.mixer.music.load("intro-pygame/assets/sounds/silbato.ogg")
pygame.mixer.music.play(1,0.0)

#efectos sonoros
Gallo = pygame.mixer.Sound("intro-pygame/assets/sounds/gallo.ogg")
Cuervo = pygame.mixer.Sound("intro-pygame/assets/sounds/cuervo.ogg")
Timbre  = pygame.mixer.Sound("intro-pygame/assets/sounds/timbre.ogg")

while continuar:
    for event in pygame.event.get():
        # cerrar ventana si hace click en la "X"
        if event.type == pygame.QUIT:
            continuar = False
        # detectar si se presiona una tecla
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuar = False
            elif event.key == pygame.K_o:
                Gallo.play()
            elif event.key == pygame.K_c:
                Cuervo.play()
            elif event.key == pygame.K_v:
                Timbre.play()

pygame.display.flip()