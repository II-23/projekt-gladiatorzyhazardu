from zmienne import *
from printbids import *

from info_o_grze import GameInfo
import dostepne_bidy

class Rozgrywka:
    stan = 3

    opacity = 255
    bids = []

    #check
    check_img = None
    button_check = None

    cards_paths = []

    scale_start = 0.22
    width_DOWN = 630 * scale_start*SCALE
    height_DOWN = 880 * scale_start*SCALE
    width_DOWN_front = 650 * scale_start*SCALE
    height_DOWN_front = 900 * scale_start*SCALE
    liczba_kart = 0
    karty = []

    szerokosc_reki = (liczba_kart+1) * width_DOWN/2
    szerokosc_reki_wysunietej = szerokosc_reki + (liczba_kart-1) * width_DOWN/2 + (liczba_kart-1) * 5

    wsp_kart = []
    wsp_kart_wysunietych = []
    wsp_kart_akt = []

    y_kart = SCREEN_HEIGHT - 3*height_DOWN/5
    y_kart_wysunietych = SCREEN_HEIGHT - height_DOWN - 5

    for i in range(liczba_kart):
        #wsp_kart.append((SCREEN_WIDTH/2 - szerokosc_reki/2 + i*width_DOWN/2, y_kart))
        wsp_kart.append((TABLE_CENTER[0] - szerokosc_reki/2 + i*width_DOWN/2, y_kart))
        wsp_kart_akt.append(wsp_kart[i])
    
    for i in range(liczba_kart):
        #wsp_kart_wysunietych.append((SCREEN_WIDTH/2 - szerokosc_reki_wysunietej/2 + i*width_DOWN + i*5, y_kart_wysunietych))
        wsp_kart_wysunietych.append((TABLE_CENTER[0] - szerokosc_reki_wysunietej/2 + i*width_DOWN + i*5, y_kart_wysunietych))
    
    czas_wysuwania = 200
    wysuwanie = 0
    #strefa_wysuwania = pygame.rect.Rect(SCREEN_WIDTH/2 - szerokosc_reki/2, SCREEN_HEIGHT - 3*height_DOWN/5, szerokosc_reki, 3*height_DOWN/5)
    strefa_wysuwania = pygame.rect.Rect(TABLE_CENTER[0] - szerokosc_reki/2, SCREEN_HEIGHT - 3*height_DOWN/5, szerokosc_reki, 3*height_DOWN/5)

    liczba_przeciwnikow = None
    liczba_kart_przeciwnikow = []
    nicki_przeciwnikow = []
    wsp_kart_przeciwnikow = []
    back = pygame.image.load("textures/b0.png")
    back = pygame.transform.scale_by(back, scale_start*SCALE)

    played_bid = None

    def karty_graczy(dane):
        liczba_graczy = len(dane.player_cards) - 1
        liczba_kart = []
        for i in range(1, liczba_graczy):
            liczba_kart.append(len(dane.player_cards[i]))
        

    def name_to_path(card_name):
        card_name = str(card_name).split(" ")
        path = "textures/"
        path += card_name[0]
        path += '-of-'
        path += card_name[2]
        path += '.png'
        return path

    def ustaw(dane: GameInfo):
        Rozgrywka.liczba_kart = len(dane.player_cards[dane.my_index])
        karty = dane.player_cards[dane.my_index]
        Rozgrywka.karty = []
        for i in range(len(karty)):
            path = Rozgrywka.name_to_path(karty[i])
            Rozgrywka.karty.append(pygame.image.load(path))
            Rozgrywka.karty[i] = pygame.transform.scale_by(Rozgrywka.karty[i], Rozgrywka.scale_start*SCALE)
        Rozgrywka.szerokosc_reki = (Rozgrywka.liczba_kart+1) * Rozgrywka.width_DOWN_front/2
        Rozgrywka.szerokosc_reki_wysunietej = Rozgrywka.szerokosc_reki + (Rozgrywka.liczba_kart-1) * Rozgrywka.width_DOWN_front/2 + (Rozgrywka.liczba_kart-1) * 5
        Rozgrywka.wsp_kart = []
        Rozgrywka.wsp_kart_wysunietych = []
        Rozgrywka.wsp_kart_akt = []
        for i in range(Rozgrywka.liczba_kart):
            #Rozgrywka.wsp_kart.append((SCREEN_WIDTH/2 - Rozgrywka.szerokosc_reki/2 + i*Rozgrywka.width_DOWN/2, Rozgrywka.y_kart))
            Rozgrywka.wsp_kart.append((TABLE_CENTER[0] - Rozgrywka.szerokosc_reki/2 + i*Rozgrywka.width_DOWN/2, Rozgrywka.y_kart))
            Rozgrywka.wsp_kart_akt.append(Rozgrywka.wsp_kart[i])
            #Rozgrywka.wsp_kart_wysunietych.append((SCREEN_WIDTH/2 - Rozgrywka.szerokosc_reki_wysunietej/2 + i*Rozgrywka.width_DOWN + i*5, Rozgrywka.y_kart_wysunietych))
            Rozgrywka.wsp_kart_wysunietych.append((TABLE_CENTER[0] - Rozgrywka.szerokosc_reki_wysunietej/2 + i*Rozgrywka.width_DOWN + i*5, Rozgrywka.y_kart_wysunietych))
        #Rozgrywka.strefa_wysuwania = pygame.rect.Rect(SCREEN_WIDTH/2 - Rozgrywka.szerokosc_reki/2, SCREEN_HEIGHT - 3*Rozgrywka.height_DOWN/5, Rozgrywka.szerokosc_reki, 3*Rozgrywka.height_DOWN/5)
        Rozgrywka.strefa_wysuwania = pygame.rect.Rect(TABLE_CENTER[0] - Rozgrywka.szerokosc_reki/2, SCREEN_HEIGHT - 3*Rozgrywka.height_DOWN/5, Rozgrywka.szerokosc_reki, 3*Rozgrywka.height_DOWN/5)

        if Rozgrywka.check_img == None:
            Rozgrywka.check_img = pygame.image.load("textures/button-check.png")
            Rozgrywka.check_img = pygame.transform.scale(Rozgrywka.check_img, (int(0.15*SCREEN_WIDTH), int(0.15*SCREEN_WIDTH)))
            Rozgrywka.button_check = Rozgrywka.check_img.get_rect()
            Rozgrywka.button_check.bottomleft=(int(27*SCALE), SCREEN_HEIGHT - int(40*SCALE))

        Rozgrywka.liczba_przeciwnikow = len(dane.players) - 1
        Rozgrywka.liczba_kart_przeciwnikow = []
        Rozgrywka.nicki_przeciwnikow = []
        Rozgrywka.wsp_kart_przeciwnikow = []
        przedzial_na_gracza = TABLE_WIDTH / Rozgrywka.liczba_przeciwnikow
        pierwszy_gracz = TABLE_CORNER[0] + przedzial_na_gracza/2 - Rozgrywka.width_DOWN/2

        for i in range(len(dane.players)):
            if dane.players[i][1] == dane.my_id:
                continue

            indeks_przeciwnika = len(Rozgrywka.liczba_kart_przeciwnikow)
            Rozgrywka.liczba_kart_przeciwnikow.append(len(dane.player_cards[i]))
            Rozgrywka.nicki_przeciwnikow.append(dane.players[i][0])
            Rozgrywka.wsp_kart_przeciwnikow.append((pierwszy_gracz + indeks_przeciwnika * przedzial_na_gracza, 80))

    def klikniecie(x, y, event=None):

        potential_bid = dostepne_bidy.handle_button_event(event)

        if potential_bid != None:
            Rozgrywka.played_bid = potential_bid

        if Rozgrywka.button_check.collidepoint(x, y):
            Rozgrywka.played_bid = "check"


    def ruch_myszki(x, y, event=None):
        if Rozgrywka.strefa_wysuwania.collidepoint(x, y):
            Rozgrywka.wysuwanie = 1
        elif not Rozgrywka.strefa_wysuwania.collidepoint(x, y):
            Rozgrywka.wysuwanie = 0
            
        potential_bid = dostepne_bidy.handle_button_event(event)

        if potential_bid != None:
            Rozgrywka.played_bid = potential_bid

    def rysuj(screen, dt: float, dane: GameInfo):
        for i in range(Rozgrywka.liczba_przeciwnikow):
            nick = Rozgrywka.nicki_przeciwnikow[i]
            font = pygame.font.SysFont("comicsansms",round(40*SCALE))
            text = font.render(nick, True, (0, 0, 0))
            text_rect = text.get_rect(center=(Rozgrywka.wsp_kart_przeciwnikow[i][0] + Rozgrywka.width_DOWN // 2, Rozgrywka.wsp_kart_przeciwnikow[i][1] - text.get_height() // 2 - 10))
            screen.blit(text, text_rect)
            screen.blit(Rozgrywka.back, Rozgrywka.wsp_kart_przeciwnikow[i])
            text = font.render(str(Rozgrywka.liczba_kart_przeciwnikow[i]), True, (0, 0, 0))
            text_rect = text.get_rect(center=(Rozgrywka.wsp_kart_przeciwnikow[i][0] + Rozgrywka.width_DOWN // 2, Rozgrywka.wsp_kart_przeciwnikow[i][1] + text.get_height() // 2 + Rozgrywka.height_DOWN + 10))
            screen.blit(text, text_rect)

        procent_wysuniecia = dt / Rozgrywka.czas_wysuwania
        for i in range(Rozgrywka.liczba_kart):
            dx = procent_wysuniecia * abs(Rozgrywka.wsp_kart_wysunietych[i][0] - Rozgrywka.wsp_kart[i][0])
            dy = procent_wysuniecia * abs(Rozgrywka.wsp_kart_wysunietych[i][1] - Rozgrywka.wsp_kart[i][1])
            if Rozgrywka.wysuwanie:
                if Rozgrywka.wsp_kart_akt[i][0] < Rozgrywka.wsp_kart_wysunietych[i][0]:
                    pom = (Rozgrywka.wsp_kart_akt[i][0] + dx, Rozgrywka.wsp_kart_akt[i][1]-dy)
                    if pom[1] <= Rozgrywka.wsp_kart_wysunietych[i][1]:
                        pom = Rozgrywka.wsp_kart_wysunietych[i]
                else:
                    pom = (Rozgrywka.wsp_kart_akt[i][0] - dx, Rozgrywka.wsp_kart_akt[i][1]-dy)
                    if pom[1] <= Rozgrywka.wsp_kart_wysunietych[i][1]:
                        pom = Rozgrywka.wsp_kart_wysunietych[i]
            else:
                if Rozgrywka.wsp_kart_akt[i][0] < Rozgrywka.wsp_kart[i][0]:
                    pom = (Rozgrywka.wsp_kart_akt[i][0] + dx, Rozgrywka.wsp_kart_akt[i][1]+dy)
                    if pom[1] >= Rozgrywka.wsp_kart[i][1]:
                        pom = Rozgrywka.wsp_kart[i]
                else:
                    pom = (Rozgrywka.wsp_kart_akt[i][0] - dx, Rozgrywka.wsp_kart_akt[i][1]+dy)
                    if pom[1] >= Rozgrywka.wsp_kart[i][1]:
                        pom = Rozgrywka.wsp_kart[i]
            Rozgrywka.wsp_kart_akt[i] = pom
            screen.blit(Rozgrywka.karty[i], Rozgrywka.wsp_kart_akt[i])
        
        if Rozgrywka.bids != dane.bid_history:
            Rozgrywka.bids = dane.bid_history
            Rozgrywka.opacity = 1
        elif Rozgrywka.opacity < 255:
            Rozgrywka.opacity += 8
            if Rozgrywka.opacity > 255:
                Rozgrywka.opacity = 255
        
        display_new_bids(screen, Rozgrywka.bids, dane.nickbid_history,Rozgrywka.opacity,(16*SCALE,40*SCALE),SCALE)

        recent_bid = None
        if len(dane.bid_history) > 0:
            recent_bid = dane.bid_history[-1]
        
        dostepne_bidy.draw_buttons(screen, recent_bid)
            
        if dane.my_index == dane.current_player:
            screen.blit(Rozgrywka.check_img, Rozgrywka.button_check)
        
