import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Poker tajski")


# Rysowanie tła

def rysuj_tlo():
    bg = pygame.image.load("kolor.png")
    pygame.Surface.blit(screen, bg, (0, 0))


# Główna pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rysuj_tlo()
    pygame.display.update()