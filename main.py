import pygame
import sys
from zmienne import *
from menu import *
from pregame import *

pygame.init()
pygame.display.set_caption("Poker tajski")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Rysowanie tła
def rysuj_tlo():
    bg = pygame.image.load("data/images/kolor.png")
    screen.blit(bg, (0, 0))
        

class Gra:
    liczba_graczy=4
    stan_gry=Menu.stan

    def cofnij_stan():
        if Gra.stan_gry==preGame.stan:
            Gra.stan_gry=Menu.stan
    

while True:
    clock.tick(60)
    rysuj_tlo()
    mouse = pygame.mouse.get_pos() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Gra.stan_gry==Menu.stan:
                Gra.stan_gry=Menu.klikniecie(mouse[0], mouse[1]) 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Gra.cofnij_stan()

    if Gra.stan_gry==Menu.stan:
        Menu.rysuj(screen)
    #if Gra.stan_gry==preGame.stan:


                

    
    pygame.display.update()