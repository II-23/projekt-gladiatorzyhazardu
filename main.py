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

def komunikacja_z_serwerem(dane):
    if not dane.nick == "" and dane.my_id == None:
            dane.my_id = client.register(dane.nick)
    if dane.admin_id == False and preGame.tworzenie_stolu == True:
        dane.table_id = client.create_table(dane.my_id)
        dane.admin_id = True
        client.join_table(dane.my_id, dane.table_id)
        
    if not dane.table_id == None:
        akt = client.get_table(dane.table_id)
        if dane.current_player == None:
            pass
            #print(akt)
        dane.players = akt['players']
        dane.current_player = akt['current_index']
        dane.player_cards = akt['cards']
    #otworzone stoly
    if preGame.dolaczanie_do_stolu == True:
        akt = client.get_all_tables()
        dane.tables = []
        for i in range(len(akt)):
            admin = client.get_table(akt[i])['admin'][1]
            players = client.get_all_players()
            for j in range(len(players)):
                if players[j] == admin:
                    admin_nick = client.id_to_nick(admin)
                    dane.tables.append((akt[i], admin_nick))
                    break
        print(dane.tables)

    #dolaczanie do stolu
    if preGame.dolaczyl == True:
        client.join_table(dane.my_id, dane.table_id)
        preGame.dolaczyl = False
        preGame.dolaczanie_do_stolu = False

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

    def klikniecie(x, y, dane):
        if Gra.stan_gry == Menu.stan:
            if Menu.klikniecie(x, y) < AKCJA:
                Gra.stan_gry = Menu.klikniecie(x, y)

        elif Gra.stan_gry == preGame.stan:
            if preGame.klikniecie(x, y, dane) < AKCJA:
                Gra.stan_gry = preGame.klikniecie(x, y, dane)

            
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

    komunikacja_z_serwerem(dane)
    if not dane.table_id == None:
        pass
        #print(dane.table_id)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # nacisniecie myszki
        if event.type == pygame.MOUSEBUTTONDOWN:
            Gra.klikniecie(mouse[0], mouse[1], dane)

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
        preGame.rysuj(screen, dane)

    elif Gra.stan_gry == Rozdanie.stan:
        Rozdanie.rysuj(screen)
    
    elif Gra.stan_gry == Rozgrywka.stan:
        Rozgrywka.rysuj(screen, dt)

    # if Gra.stan_gry==preGame.stan:

    pygame.display.update()
