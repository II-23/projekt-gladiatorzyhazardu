import pygame
import sys
from client import client
from zmienne import *
from menu import *
from pregame import *
from rozgrywka import *
from rozdanie import *
from info_o_grze import *
from pygame.locals import *

dane = game_info()

pygame.init()
pygame.display.set_caption("Poker tajski")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN)


# Rysowanie tła
def rysuj_tlo():
    bg = pygame.image.load("data/images/kolor.png")
    screen.blit(bg, (0, 0))


class Gra:
    #liczba_graczy = 2
    stan_gry = Menu.stan

    def cofnij_stan():
        if Gra.stan_gry == preGame.stan:
            Gra.stan_gry = Menu.stan

    def klikniecie(x, y):
        if Gra.stan_gry == Menu.stan:
            if Menu.klikniecie(x, y) < AKCJA:
                Gra.stan_gry = Menu.klikniecie(x, y)

        elif Gra.stan_gry == preGame.stan:
            if preGame.klikniecie(x, y) < AKCJA:
                Gra.stan_gry = preGame.klikniecie(x, y)

            
    def puszczenie():
        if Gra.stan_gry == preGame.stan:
            preGame.puszczenie()

    def ruch_myszki(x, y):
        if Gra.stan_gry == preGame.stan:
            preGame.ruch_myszki(x, y)
        if Gra.stan_gry == Rozgrywka.stan:
            Rozgrywka.ruch_myszki(x, y)
    def wpisywanie(key, dane):
        if Gra.stan_gry == preGame.stan:
            preGame.wpisywanie(key, dane)


while True:
    dt = clock.tick(60)
    rysuj_tlo()
    mouse = pygame.mouse.get_pos()

    if not dane.nick == "" and dane.my_id == None:
        dane.my_id = client.register(dane.nick)

    print(dane.my_id)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # nacisniecie myszki
        if event.type == pygame.MOUSEBUTTONDOWN:
            Gra.klikniecie(mouse[0], mouse[1])

        # puszczenie myszki
        if event.type == pygame.MOUSEBUTTONUP:
            Gra.puszczenie()

        # klawiatura
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Gra.cofnij_stan()
            else:
                Gra.wpisywanie(event.key, dane)

        # ruch myszki
        if event.type == pygame.MOUSEMOTION:
            Gra.ruch_myszki(mouse[0], mouse[1])

    if Gra.stan_gry == Menu.stan:
        Menu.rysuj(screen)

    elif Gra.stan_gry == preGame.stan:
        preGame.rysuj(screen)

    elif Gra.stan_gry == Rozdanie.stan:
        Rozdanie.rysuj(screen)
    
    elif Gra.stan_gry == Rozgrywka.stan:
        Rozgrywka.rysuj(screen, dt)

    # if Gra.stan_gry==preGame.stan:

    pygame.display.update()
