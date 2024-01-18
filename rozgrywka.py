from zmienne import *
from printbids import *

class Rozgrywka:
    stan = 3

    # RECTANGLE_WIDTH, RECTANGLE_HEIGHT = 312, 75
    # MARGIN = 2
    # BACKGROUND_COLOR = (200, 200, 200)
    # RECTANGLE_COLOR = (100, 100, 255)
    # TEXT_COLOR = (0, 0, 0)
    # font_bids =pygame.font.SysFont("comicsansms",26) #font to be set
    opacity = 255
    bids = []

    #check
    check_img = None
    button_check = None

    cards_paths = []


    scale_start = 0.22
    width_DOWN = 630 * scale_start
    height_DOWN = 880 * scale_start
    width_DOWN_front = 650 * scale_start
    height_DOWN_front = 900 * scale_start
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
    back = pygame.transform.scale_by(back, scale_start)

    # #Autor : Xaro8
    # # use this function when no new bid was played(every time normal fps display)needs surface,list of bids, starting position and  scale is optional
    # def display_bids(screen,strings,start_pos=(15,40),scale=1.0):

    #     strings=strings[::-1]
    #     strings=strings[:min(len(strings),8)]
    #     shape_img=pygame.image.load("textures/shape.png")
    #     shape_img=pygame.transform.scale(shape_img,(Rozgrywka.RECTANGLE_WIDTH*scale, Rozgrywka.RECTANGLE_HEIGHT*scale))
    #     shape= shape_img.get_rect()

    
    #     y_position = start_pos[1]
    #     for string in strings:
    #         text = Rozgrywka.font_bids.render(string, True, Rozgrywka.TEXT_COLOR)
    #         shape.topleft=(start_pos[0],y_position)
    #         text_rect = text.get_rect(center=shape.center)

    #         screen.blit(shape_img,shape)
    #         screen.blit(text, text_rect)

    #         y_position += Rozgrywka.RECTANGLE_HEIGHT*scale + 2 * Rozgrywka.MARGIN*scale  # Add some spacing

    # #use when new bid was played needs surface,list of bids, starting position and  scale is optional
    # def display_new_bids(screen,strings,start_pos=(15,40),scale=1.0):
    #     if len(strings)==0: return
    #     # strings=strings[::-1]
    #     strings=strings[len(strings)-min(len(strings),8):]

    #     shape_img=pygame.image.load("textures/shape.png")
    #     shape_img=pygame.transform.scale(shape_img,(Rozgrywka.RECTANGLE_WIDTH*scale, Rozgrywka.RECTANGLE_HEIGHT*scale))
    #     shape= shape_img.get_rect()
    #     opacity=1
    #     while opacity<=256:
        
    #         shape_img.set_alpha(opacity)
    #         text = Rozgrywka.font_bids.render(strings[len(strings)-1], True, Rozgrywka.TEXT_COLOR)
    #         text.set_alpha(opacity)
        
    #         shape.topleft=(start_pos[0],start_pos[1])
    #         text_rect = text.get_rect(center=shape.center)
            
    #         screen.blit(shape_img,shape)
    #         screen.blit(text, text_rect)
    #         Rozgrywka.display_bids(screen,strings[:len(strings)-1],(start_pos[0],start_pos[1]+ Rozgrywka.RECTANGLE_HEIGHT*scale + 2 * Rozgrywka.MARGIN*scale),scale)
    #         time.sleep(1/30)
    #         opacity+=5



    #def klikniecie(x, y):
        
        
    #def puszczenie():

    def karty_graczy(dane):
        liczba_graczy = len(dane.player_cards) - 1
        liczba_kart = []
        for i in range(1, liczba_graczy):
            liczba_kart.append(len(dane.player_cards[i]))
        

    def name_to_path(card_name):
        card_name = card_name.split(" ")
        path = "textures/"
        path += card_name[0]
        path += '-of-'
        path += card_name[2]
        path += '.png'
        return path

    def ustaw(dane):
        Rozgrywka.liczba_kart = len(dane.player_cards[dane.my_index])
        karty = dane.player_cards[dane.my_index]
        Rozgrywka.karty = []
        for i in range(len(karty)):
            path = Rozgrywka.name_to_path(karty[i])
            Rozgrywka.karty.append(pygame.image.load(path))
            Rozgrywka.karty[i] = pygame.transform.scale_by(Rozgrywka.karty[i], Rozgrywka.scale_start)
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
            Rozgrywka.check_img = pygame.transform.scale(Rozgrywka.check_img, (int(0.1*SCREEN_WIDTH), int(0.1*SCREEN_WIDTH)))
            Rozgrywka.button_check = Rozgrywka.check_img.get_rect()

        Rozgrywka.liczba_przeciwnikow = len(dane.player_cards) - 1
        Rozgrywka.liczba_kart_przeciwnikow = []
        Rozgrywka.nicki_przeciwnikow = []
        Rozgrywka.wsp_kart_przeciwnikow = []
        przedzial_na_gracza = TABLE_WIDTH / Rozgrywka.liczba_przeciwnikow
        pierwszy_gracz = TABLE_CORNER[0] + przedzial_na_gracza/2 - Rozgrywka.width_DOWN/2
        for i in range(1, Rozgrywka.liczba_przeciwnikow + 1):
            Rozgrywka.liczba_kart_przeciwnikow.append(len(dane.player_cards[i]))
            Rozgrywka.nicki_przeciwnikow.append(dane.players[i][0])
            Rozgrywka.wsp_kart_przeciwnikow.append((pierwszy_gracz + (i-1)*przedzial_na_gracza, 80))
            

    def ruch_myszki(x, y):
        if Rozgrywka.strefa_wysuwania.collidepoint(x, y):
            Rozgrywka.wysuwanie = 1
        elif not Rozgrywka.strefa_wysuwania.collidepoint(x, y):
            Rozgrywka.wysuwanie = 0
        

    def rysuj(screen, dt, dane):
        for i in range(Rozgrywka.liczba_przeciwnikow):
            #nick nad karta
            nick = Rozgrywka.nicki_przeciwnikow[i]
            font=pygame.font.SysFont("comicsansms",40)
            text = font.render(nick, True, (0, 0, 0))
            text_rect = text.get_rect(center=(Rozgrywka.wsp_kart_przeciwnikow[i][0] + Rozgrywka.width_DOWN // 2, Rozgrywka.wsp_kart_przeciwnikow[i][1] - text.get_height() // 2 - 10))
            screen.blit(text, text_rect)
            screen.blit(Rozgrywka.back, Rozgrywka.wsp_kart_przeciwnikow[i])
            text = font.render(str(Rozgrywka.liczba_kart_przeciwnikow[i]), True, (0, 0, 0))
            text_rect = text.get_rect(center=(Rozgrywka.wsp_kart_przeciwnikow[i][0] + Rozgrywka.width_DOWN // 2, Rozgrywka.wsp_kart_przeciwnikow[i][1] + text.get_height() // 2 + Rozgrywka.height_DOWN + 10))
            screen.blit(text, text_rect)

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
            #print(i)
            screen.blit(Rozgrywka.karty[i], Rozgrywka.wsp_kart_akt[i])
            #screen.blit(Rozgrywka.karty[i], Rozgrywka.wsp_kart[i])
            #screen.blit(Rozgrywka.karty[i], Rozgrywka.wsp_kart_wysunietych[i])
            #Rozgrywka.bids.append("wawrzyn")
        

        #Rozgrywka.bids = ["wawrzyn", "dwa", "XD"]
        if Rozgrywka.bids != dane.bid_history:
            Rozgrywka.bids = dane.bid_history
            #dane.bid_history = Rozgrywka.bids
            Rozgrywka.opacity = 1
        elif Rozgrywka.opacity < 255:
            Rozgrywka.opacity += 5
            if Rozgrywka.opacity > 255:
                Rozgrywka.opacity = 255
        
        display_new_bids(screen, Rozgrywka.bids, Rozgrywka.opacity)
            
        if dane.my_index == dane.current_player:
            screen.blit(Rozgrywka.check_img, (20, SCREEN_HEIGHT - 20 - Rozgrywka.check_img.get_height()))
        
