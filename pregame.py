from zmienne import *

class preGame:
    stan=1
    nacisniety_suwak=False
    poprzedni_x=0
    liczba_graczy=2

    #menu
    glowny=pygame.rect.Rect(50, 50, SCREEN_WIDTH-100, SCREEN_HEIGHT-100)
    #tytuł
    font=pygame.font.SysFont("comicsansms", 120)
    tytul = font.render("Ilu graczy?", True, DARK_RED)


    #belka suwaka
    belka=(SCREEN_WIDTH//10, 200, 8*SCREEN_WIDTH//10, 25)
    #suwak
    suwak_x=SCREEN_WIDTH//5
    
    suwak=pygame.rect.Rect(suwak_x, 190, 70, 45)

    font_licznik=pygame.font.SysFont("comicsansms", 80)
    licznik = font_licznik.render(str(liczba_graczy), True, BLACK)
    

    def aktualizuj_licznik():
        #liczba graczy
        dlugosc_podzialu=(SCREEN_WIDTH-170)//9
        srodek_suwaka_bezwzgl=preGame.suwak_x+35
        preGame.liczba_graczy=srodek_suwaka_bezwzgl//dlugosc_podzialu
        preGame.font=pygame.font.SysFont("comicsansms", 80)
        preGame.licznik = preGame.font.render(str(preGame.liczba_graczy), True, BLACK)



    def aktualizuj_suwak(przesuniecie, x):
        preGame.suwak_x+=przesuniecie
        if x<50:
            preGame.suwak_x=50
        elif x>SCREEN_WIDTH-50:
            preGame.suwak_x=SCREEN_WIDTH-50-70
        if preGame.suwak_x<50:
            preGame.suwak_x=50
        elif preGame.suwak_x>SCREEN_WIDTH-50-70:
            preGame.suwak_x=SCREEN_WIDTH-50-70
        preGame.suwak=pygame.rect.Rect(preGame.suwak_x, 190, 70, 45)
        
        preGame.aktualizuj_licznik()

    def klikniecie(x, y):
        #suwak
        if preGame.suwak.collidepoint(x, y):
            preGame.nacisniety_suwak=True
    
    def puszczenie():
        preGame.nacisniety_suwak=False

    def ruch_myszki(x, y):
        if preGame.nacisniety_suwak:
            przesuniecie=x-preGame.poprzedni_x
            preGame.aktualizuj_suwak(przesuniecie, x)
        
        preGame.poprzedni_x=x

    def rysuj(screen):
        pygame.draw.rect(screen, GREY, preGame.glowny)
        screen.blit(preGame.tytul, (SCREEN_WIDTH//2 - preGame.tytul.get_width() // 2, SCREEN_HEIGHT//5 - preGame.tytul.get_height() // 2))

        pygame.draw.rect(screen, DARK_GREY, preGame.belka)
        pygame.draw.rect(screen, DARK_RED, preGame.suwak)

        screen.blit(preGame.licznik, (preGame.suwak_x+35-preGame.licznik.get_width()//2, 240))

