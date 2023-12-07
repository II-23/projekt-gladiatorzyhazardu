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
    max_stanow=1

    def cofnij_stan():
        if Gra.stan_gry==preGame.stan:
            Gra.stan_gry=Menu.stan

    def klikniecie(x, y):
        if Gra.stan_gry==Menu.stan:
            if Menu.klikniecie(x, y)<=Gra.max_stanow:
                Gra.stan_gry=Menu.klikniecie(x, y)

        elif Gra.stan_gry==preGame.stan:
            preGame.klikniecie(x, y)

    def puszczenie():
        if Gra.stan_gry == preGame.stan:
            preGame.puszczenie()

    
    def ruch_myszki(x, y):
        if Gra.stan_gry == preGame.stan:
            preGame.ruch_myszki(x, y)


    

while True:
    clock.tick(60)
    rysuj_tlo()
    mouse = pygame.mouse.get_pos() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #nacisniecie myszki
        if event.type == pygame.MOUSEBUTTONDOWN:
            Gra.klikniecie(mouse[0], mouse[1])

        #puszczenie myszki
        if event.type == pygame.MOUSEBUTTONUP:
            Gra.puszczenie()

        #klawiatura
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Gra.cofnij_stan()

        #ruch myszki
        if event.type == pygame.MOUSEMOTION:
            Gra.ruch_myszki(mouse[0], mouse[1])
            


    if Gra.stan_gry==Menu.stan:
        Menu.rysuj(screen)

    elif Gra.stan_gry==preGame.stan:
        preGame.rysuj(screen)



    #if Gra.stan_gry==preGame.stan:


                

    
    pygame.display.update()