from zmienne import *


class preGame:
    stan = 1
    nacisniety_suwak = False
    poprzedni_x = 0
    max_dl_nicku = 8
    nick = ""
    tworzenie_stolu = False
    dolaczanie_do_stolu = False

    # menu
    glowny = pygame.rect.Rect(50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100)

    # tytuł
    font = pygame.font.SysFont("comicsansms", 120)
    tytul = font.render("Wprowadź nick", True, DARK_RED)
    napis_nick = font.render("Nick: " + nick, True, DARK_RED)

    # Start
    font = pygame.font.SysFont("comicsansms", 100)
    start_napis = font.render("Start", True, DARK_RED)
    start_corner = (
        SCREEN_WIDTH // 2 - start_napis.get_width() // 2,
        4 * SCREEN_HEIGHT // 5 - start_napis.get_height() // 2,
    )
    start_button = pygame.rect.Rect(
        start_corner[0] - 25,
        start_corner[1] - 10,
        start_napis.get_width() + 50,
        start_napis.get_height() + 20,
    )

    towrzenie_button = pygame.rect.Rect(1*SCREEN_WIDTH//5, 3*SCREEN_HEIGHT//5, SCREEN_WIDTH//5, SCREEN_HEIGHT//4)
    dolaczanie_button = pygame.rect.Rect(3*SCREEN_WIDTH//5 , 3*SCREEN_HEIGHT//5, SCREEN_WIDTH//5, SCREEN_HEIGHT//4)
    tworzenie_napis = font.render("Stwórz", True, DARK_RED)
    dolaczanie_napis = font.render("Dołącz", True, DARK_RED)

    #start_button = pygame.rect.Rect(SCREEN_WIDTH // 2 - 100, 4*SCREEN_HEIGHT // 5 - 50, 200, 100)

    #liczba graczy przy stole
    def startowanie_rys(screen, liczba_graczy):
        font = pygame.font.SysFont("comicsansms", 100)
        liczba_graczy_napis = font.render("Liczba graczy: " + str(liczba_graczy), True, DARK_RED)
        screen.blit(liczba_graczy_napis, (SCREEN_WIDTH // 2 - liczba_graczy_napis.get_width() // 2, 3*SCREEN_HEIGHT // 5 - liczba_graczy_napis.get_height() // 2))
        
        pygame.draw.rect(screen, DARK_GREY, preGame.start_button)
        screen.blit(preGame.start_napis, preGame.start_corner)


    def klikniecie(x, y, dane):
        # przejscie do rozdania kart
        if preGame.dolaczanie_do_stolu == False and preGame.tworzenie_stolu == False:
            if preGame.dolaczanie_button.collidepoint(x, y):
                preGame.dolaczanie_do_stolu = True
            if preGame.towrzenie_button.collidepoint(x, y):
                preGame.tworzenie_stolu = True
        if dane.admin_id and preGame.start_button.collidepoint(x, y):
            return 3
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
            preGame.napis_nick = preGame.font.render("Nick: " + preGame.nick, True, DARK_RED)


    def rysuj(screen, dane):
        pygame.draw.rect(screen, GREY, preGame.glowny)
        
        #if dane.my_id == None:
        
        if preGame.dolaczanie_do_stolu == False and preGame.tworzenie_stolu == False:
            screen.blit(preGame.tytul,(SCREEN_WIDTH // 2 - preGame.tytul.get_width() // 2,SCREEN_HEIGHT // 5 - preGame.tytul.get_height() // 2,))
            screen.blit(preGame.napis_nick,(SCREEN_WIDTH // 2 - preGame.napis_nick.get_width() // 2,SCREEN_HEIGHT // 2 - preGame.napis_nick.get_height() // 2,))
            if not dane.my_id == None:
                pygame.draw.rect(screen, DARK_GREY, preGame.dolaczanie_button)
                pygame.draw.rect(screen, BLACK, preGame.dolaczanie_button, 5)
                screen.blit(preGame.dolaczanie_napis, (3*SCREEN_WIDTH//5 + preGame.dolaczanie_button.width//2 - preGame.dolaczanie_napis.get_width()//2, 3*SCREEN_HEIGHT//5 + preGame.dolaczanie_button.height//2 - preGame.dolaczanie_napis.get_height()//2))
                
                pygame.draw.rect(screen, DARK_GREY, preGame.towrzenie_button)
                pygame.draw.rect(screen, BLACK, preGame.towrzenie_button, 5)
                screen.blit(preGame.tworzenie_napis, (1*SCREEN_WIDTH//5 + preGame.towrzenie_button.width//2 - preGame.tworzenie_napis.get_width()//2, 3*SCREEN_HEIGHT//5 + preGame.towrzenie_button.height//2 - preGame.tworzenie_napis.get_height()//2))
        
        elif dane.admin_id:
            preGame.startowanie_rys(screen, len(dane.players))

        #pygame.draw.rect(screen, DARK_GREY, preGame.belka)
        #pygame.draw.rect(screen, DARK_RED, preGame.suwak)

        #screen.blit(preGame.licznik,(preGame.suwak_x + 35 - preGame.licznik.get_width() // 2, 240))

        # start
        #pygame.draw.rect(screen, DARK_GREY, preGame.start_button)
        #pygame.draw.rect(screen, BLACK, preGame.start_button, 5)
        #screen.blit(preGame.start_napis, preGame.start_corner)