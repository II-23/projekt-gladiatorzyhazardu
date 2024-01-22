from zmienne import *


class preGame:
    stan = 1
    nacisniety_suwak = False
    poprzedni_x = 0
    max_dl_nicku = 8
    nick = ""
    tworzenie_stolu = False
    dolaczanie_do_stolu = False
    dolaczyl = False
    wlaczenie_gry = False

    # menu
    glowny_img=pygame.image.load("textures/background-table.png")
    glowny_img= pygame.transform.scale(glowny_img,(SCREEN_WIDTH, SCREEN_HEIGHT))  
    glowny = glowny_img.get_rect(topleft=(0,0))

    # tytuł
    font = pygame.font.SysFont("comicsansms", round(120*SCALE))
    tytul = font.render("Wprowadź nick", True, (253,14,53))
    napis_nick = font.render("Nick: " + nick, True, (253,14,53))

    # Start
    font = pygame.font.SysFont("comicsansms", round(120*SCALE))
    start_napis = font.render("Start", True, (253,14,53))
    start_corner = (
        SCREEN_WIDTH // 2,
        4 * SCREEN_HEIGHT // 5
    )
  
    twob_img1=pygame.image.load("textures/button-rest.png")
    twob_img=pygame.transform.scale(twob_img1,(twob_img1.get_width()*0.2*SCALE,twob_img1.get_height()*0.2*SCALE))
    start_img=pygame.transform.scale(twob_img,(twob_img1.get_width()*0.15*SCALE,twob_img1.get_height()*0.15*SCALE))
    
    start_button=start_img.get_rect(center=start_corner)
    tworzenie_button = twob_img.get_rect(topleft=(3*SCREEN_WIDTH//5,3*SCREEN_HEIGHT//5))
    dolaczanie_button =twob_img.get_rect(topleft=(1*SCREEN_WIDTH//5,3*SCREEN_HEIGHT//5))
    tworzenie_napis = font.render("Stwórz", True, (253,14,53))
    dolaczanie_napis = font.render("Dołącz", True, (253,14,53))

    tworzenie_napis_re= tworzenie_napis.get_rect(center=tworzenie_button.center)
    dolaczanie_napis_re= dolaczanie_napis.get_rect(center=dolaczanie_button.center)    
    start_napis_re=start_napis.get_rect(center=start_button.center)
    #start_button = pygame.rect.Rect(SCREEN_WIDTH // 2 - 100, 4*SCREEN_HEIGHT // 5 - 50, 200, 100)
    
    stoly = []

    def lista_stolow_rys(screen, dane):
        if dane.tables:
            liczba_stolow = len(dane.tables)
            preGame.stoly = []
            for i in range(liczba_stolow):
                preGame.stoly.append(pygame.rect.Rect(SCREEN_WIDTH//2 - 200, 100 + 100*i, 400, 80))
                pygame.draw.rect(screen, DARK_GREY, preGame.stoly[i])
                pygame.draw.rect(screen, BLACK, preGame.stoly[i], 5)
                font = pygame.font.SysFont("comicsansms", round(50*SCALE))
                napis = font.render(dane.tables[i][1], True, DARK_RED)
                screen.blit(napis, (SCREEN_WIDTH//2 - napis.get_width()//2, 100 + 100*i + 40 - napis.get_height()//2))

    #liczba graczy przy stole
    def startowanie_rys(screen, liczba_graczy):
        font = pygame.font.SysFont("comicsansms", round(100*SCALE))
        liczba_graczy_napis = font.render("LICZBA GRACZY: " + str(liczba_graczy), True, (253,14,53))
        screen.blit(liczba_graczy_napis, (SCREEN_WIDTH // 2 - liczba_graczy_napis.get_width() // 2, 3*SCREEN_HEIGHT // 5 - liczba_graczy_napis.get_height() // 2))
        
        # pygame.draw.rect(screen, DARK_GREY, preGame.start_button)s
        screen.blit(preGame.start_img,preGame.start_button)
        screen.blit(preGame.start_napis, preGame.start_napis_re)

    def oczekiwanie_rys(screen, liczba_graczy):
        font = pygame.font.SysFont("comicsansms", round(100*SCALE))
        oczekiwanie_napis=font.render("OCZEKIWANIE NA ROZPOCZĘCIE GRY", True, (253,14,53))
        liczba_graczy_napis = font.render("LICZBA GRACZY: " + str(liczba_graczy), True, (253,14,53))
        screen.blit(oczekiwanie_napis, (SCREEN_WIDTH // 2 - oczekiwanie_napis.get_width() // 2, 3*SCREEN_HEIGHT // 5 - 100*SCALE))
        screen.blit(liczba_graczy_napis, (SCREEN_WIDTH // 2 - liczba_graczy_napis.get_width() // 2, 3*SCREEN_HEIGHT // 5 + 40*SCALE))
      

    def klikniecie(x, y, dane):
        # przejscie do rozdania kart
        if preGame.dolaczanie_do_stolu == False and preGame.tworzenie_stolu == False:
            if preGame.dolaczanie_button.collidepoint(x, y):
                preGame.dolaczanie_do_stolu = True
            if preGame.tworzenie_button.collidepoint(x, y):
                preGame.tworzenie_stolu = True
        if dane.admin_id and preGame.start_button.collidepoint(x, y):
            preGame.wlaczenie_gry = True
        if preGame.dolaczanie_do_stolu:
            for i in range(len(preGame.stoly)):
                if preGame.stoly[i].collidepoint(x, y):
                    dane.table_id = dane.tables[i][0]
                    dane.admin_id = False
                    preGame.dolaczyl = True
        return AKCJA
        
    def puszczenie():
        pass
    def ruch_myszki(x, y):
        pass

    def wpisywanie(key, dane):
        if dane.nick == "":
            if (key >= ord('a') and key <= ord('z')) or (key >= ord('0') and key <= ord('9')):
                if len(preGame.nick) < preGame.max_dl_nicku:
                    preGame.nick += chr(key)
                    print(preGame.nick)
            elif key == ord('\b') and len(preGame.nick) > 0:
                preGame.nick = preGame.nick[:-1]
                print(preGame.nick)
            elif key == ord('\r'):
                dane.nick = preGame.nick
                print(preGame.nick)
            preGame.napis_nick = preGame.font.render("Nick: " + preGame.nick, True, (253,14,53))


    def rysuj(screen, dane):
        screen.blit(preGame.glowny_img,preGame.glowny)
        
        #if dane.my_id == None:
        
        if dane.admin_id == False and preGame.dolaczanie_do_stolu == False and preGame.dolaczyl == False:
            screen.blit(preGame.tytul,(SCREEN_WIDTH // 2 - preGame.tytul.get_width() // 2,SCREEN_HEIGHT // 5 - preGame.tytul.get_height() // 2,))
            screen.blit(preGame.napis_nick,(SCREEN_WIDTH // 2 - preGame.napis_nick.get_width() // 2,SCREEN_HEIGHT // 2 - preGame.napis_nick.get_height(),))
            if not dane.my_id == None:
                screen.blit(preGame.twob_img,preGame.dolaczanie_button)
                screen.blit(preGame.dolaczanie_napis,preGame.dolaczanie_napis_re)
                
                screen.blit(preGame.twob_img,preGame.tworzenie_button)
                screen.blit(preGame.tworzenie_napis, preGame.tworzenie_napis_re)
        
        elif dane.admin_id:
            preGame.startowanie_rys(screen, len(dane.players))
        elif preGame.dolaczanie_do_stolu:
            preGame.lista_stolow_rys(screen, dane)
        elif preGame.dolaczyl:
            preGame.oczekiwanie_rys(screen, len(dane.players))

        #pygame.draw.rect(screen, DARK_GREY, preGame.belka)
        #pygame.draw.rect(screen, DARK_RED, preGame.suwak)

        #screen.blit(preGame.licznik,(preGame.suwak_x + 35 - preGame.licznik.get_width() // 2, 240))

        # start
        #pygame.draw.rect(screen, DARK_GREY, preGame.start_button)
        #pygame.draw.rect(screen, BLACK, preGame.start_button, 5)
        #screen.blit(preGame.start_napis, preGame.start_corner)