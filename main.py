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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED|pygame.FULLSCREEN)

def komunikacja_z_serwerem(dane):
    #rejestracja
    if not dane.nick == "" and dane.my_id == None:
            dane.my_id = client.register(dane.nick)
    
    #tworzenie stolu
    if dane.admin_id == False and preGame.tworzenie_stolu == True:
        dane.table_id = client.create_table(dane.my_id)
        dane.admin_id = True
        akt  = client.get_table(dane.table_id)
        for i in range(len(akt['players'])):
            if akt['players'][i][1] == dane.my_id:
                dane.my_index = i
                break

    #aktualizacja danych
    if not dane.table_id == None:
        akt = client.get_table(dane.table_id)
        dane.players = akt['players']
        dane.current_player = akt['current_index']
        dane.player_cards = akt['cards']
        dane.start_game = akt['game_started']
        dane.bid_history = akt['bids']

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
    if preGame.dolaczyl == True and preGame.dolaczanie_do_stolu == True:
        client.join_table(dane.my_id, dane.table_id)
        preGame.dolaczanie_do_stolu = False
        akt = client.get_table(dane.table_id)
        for i in range(len(akt['players'])):
            if akt['players'][i][1] == dane.my_id:
                dane.my_index = i
                break

    #startowanie gry
    if preGame.wlaczenie_gry == True:
        client.start_game(dane.my_id, dane.table_id)
        preGame.wlaczenie_gry = False
        
    


# Rysowanie tła
bg_start = pygame.image.load("textures/background-start.png")
bg_game = pygame.image.load("textures/background-game.png").convert()
bg_game = pygame.transform.scale(bg_game, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_start=pygame.transform.scale(bg_start, (SCREEN_WIDTH, SCREEN_HEIGHT))
def rysuj_tlo(stan):
    if stan != Rozgrywka.stan and stan != Rozdanie.stan:
        screen.blit(bg_start, (0, 0))
    else:
        screen.blit(bg_game, (0, 0))

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
    dt = clock.tick(30)
    rysuj_tlo(Gra.stan_gry)
    mouse = pygame.mouse.get_pos()

    #print(client.get_all_tables())

    komunikacja_z_serwerem(dane)
    if not dane.table_id == None:
        pass
        #print(dane.table_id)
    if Gra.stan_gry == preGame.stan:
        if dane.start_game:
            Gra.stan_gry = Rozdanie.stan
            Rozdanie.ustaw(dane)
    if Gra.stan_gry == Rozdanie.stan:
        if Rozdanie.czas_przejscia <= 0:
            Gra.stan_gry = Rozgrywka.stan
            Rozgrywka.ustaw(dane)


    print(dane.player_cards)

        
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
        Rozdanie.rysuj(screen, dt)
    
    elif Gra.stan_gry == Rozgrywka.stan:
        Rozgrywka.rysuj(screen, dt, dane)

    # if Gra.stan_gry==preGame.stan:

    pygame.display.update()
