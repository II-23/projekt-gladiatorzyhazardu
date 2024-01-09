from zmienne import *


class preGame:
    stan = 1
    nacisniety_suwak = False
    poprzedni_x = 0
    liczba_graczy = 2
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



    def klikniecie(x, y):
        # przejscie do rozdania kart
        if preGame.start_button.collidepoint(x, y):
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


    def rysuj(screen):
        pygame.draw.rect(screen, GREY, preGame.glowny)
        screen.blit(preGame.tytul,(SCREEN_WIDTH // 2 - preGame.tytul.get_width() // 2,SCREEN_HEIGHT // 5 - preGame.tytul.get_height() // 2,))
        screen.blit(preGame.napis_nick,(SCREEN_WIDTH // 2 - preGame.napis_nick.get_width() // 2,SCREEN_HEIGHT // 2 - preGame.napis_nick.get_height() // 2,))

        #pygame.draw.rect(screen, DARK_GREY, preGame.belka)
        #pygame.draw.rect(screen, DARK_RED, preGame.suwak)

        #screen.blit(preGame.licznik,(preGame.suwak_x + 35 - preGame.licznik.get_width() // 2, 240))

        # start
        pygame.draw.rect(screen, DARK_GREY, preGame.start_button)
        pygame.draw.rect(screen, BLACK, preGame.start_button, 5)
        screen.blit(preGame.start_napis, preGame.start_corner)