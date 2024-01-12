from zmienne import *

class Rozgrywka:
    stan = 3

    cards_paths = []


    scale_start = 0.22
    width_DOWN = 630 * scale_start
    height_DOWN = 880 * scale_start
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
        wsp_kart.append((SCREEN_WIDTH/2 - szerokosc_reki/2 + i*width_DOWN/2, y_kart))
        wsp_kart_akt.append(wsp_kart[i])
    
    for i in range(liczba_kart):
        wsp_kart_wysunietych.append((SCREEN_WIDTH/2 - szerokosc_reki_wysunietej/2 + i*width_DOWN + i*5, y_kart_wysunietych))
    
    czas_wysuwania = 200
    wysuwanie = 0
    strefa_wysuwania = pygame.rect.Rect(SCREEN_WIDTH/2 - szerokosc_reki/2, SCREEN_HEIGHT - 3*height_DOWN/5, szerokosc_reki, 3*height_DOWN/5)
    
    #def klikniecie(x, y):
        
        
    #def puszczenie():
    def name_to_path(card_name):
        card_name = card_name.split(" ")
        path = "textures/texturesX/"
        if card_name[0] == "ace":
            path += "A"
        elif card_name[0] == "king":
            path += "K"
        elif card_name[0] == "queen":
            path += "Q"
        elif card_name[0] == "jack":
            path += "J"
        elif card_name[0] == "ten":
            path += "10"
        elif card_name[0] == "nine":
            path += "9"
        if card_name[2] == "clubs":
            path += "clubsX.png"
        elif card_name[2] == "diamonds":
            path += "diamondsX.png"
        elif card_name[2] == "hearts":
            path += "heartsX.png"
        elif card_name[2] == "spades":
            path += "spadesX.png"
        return path

    def ustaw(dane):
        Rozgrywka.liczba_kart = len(dane.player_cards[dane.my_index])
        karty = dane.player_cards[dane.my_index]
        Rozgrywka.karty = []
        for i in range(len(karty)):
            path = Rozgrywka.name_to_path(karty[i])
            Rozgrywka.karty.append(pygame.image.load(path))
            Rozgrywka.karty[i] = pygame.transform.scale_by(Rozgrywka.karty[i], Rozgrywka.scale_start)
        Rozgrywka.szerokosc_reki = (Rozgrywka.liczba_kart+1) * Rozgrywka.width_DOWN/2
        Rozgrywka.szerokosc_reki_wysunietej = Rozgrywka.szerokosc_reki + (Rozgrywka.liczba_kart-1) * Rozgrywka.width_DOWN/2 + (Rozgrywka.liczba_kart-1) * 5
        Rozgrywka.wsp_kart = []
        Rozgrywka.wsp_kart_wysunietych = []
        Rozgrywka.wsp_kart_akt = []
        for i in range(Rozgrywka.liczba_kart):
            Rozgrywka.wsp_kart.append((SCREEN_WIDTH/2 - Rozgrywka.szerokosc_reki/2 + i*Rozgrywka.width_DOWN/2, Rozgrywka.y_kart))
            Rozgrywka.wsp_kart_akt.append(Rozgrywka.wsp_kart[i])
            Rozgrywka.wsp_kart_wysunietych.append((SCREEN_WIDTH/2 - Rozgrywka.szerokosc_reki_wysunietej/2 + i*Rozgrywka.width_DOWN + i*5, Rozgrywka.y_kart_wysunietych))
        Rozgrywka.strefa_wysuwania = pygame.rect.Rect(SCREEN_WIDTH/2 - Rozgrywka.szerokosc_reki/2, SCREEN_HEIGHT - 3*Rozgrywka.height_DOWN/5, Rozgrywka.szerokosc_reki, 3*Rozgrywka.height_DOWN/5)

    def ruch_myszki(x, y):
        if Rozgrywka.strefa_wysuwania.collidepoint(x, y):
            Rozgrywka.wysuwanie = 1
        elif not Rozgrywka.strefa_wysuwania.collidepoint(x, y):
            Rozgrywka.wysuwanie = 0
        

    def rysuj(screen, dt):
        procent_wysuniecia = dt / Rozgrywka.czas_wysuwania
        for i in range(Rozgrywka.liczba_kart):
            #droga_calkowita = (Rozgrywka.wsp_kart_wysunietych[i][0]**2 - Rozgrywka.wsp_kart[i][0]**2)**(1/2)
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
            print(i)
            screen.blit(Rozgrywka.karty[i], Rozgrywka.wsp_kart_akt[i])
            #screen.blit(Rozgrywka.karty[i], Rozgrywka.wsp_kart[i])
            #screen.blit(Rozgrywka.karty[i], Rozgrywka.wsp_kart_wysunietych[i])

        print("Rysuje rozgrywke")
