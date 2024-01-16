from zmienne import *

class Rozdanie:
    stan = 2
    liczba_kart = 3
    zwiekszanie = 1
    zmniejszanie = 0
    zmniejszanie_tasowanej = 0
    prawo = 0
    lewo = 0
    kart_do_tasowania = 4
    animacja_tasowania = 1
    animacja_rozdawania = 0

    scaleUP = 1.1
    scale_start = 0.22
    width_DOWN = 630 * scale_start
    height_DOWN = 880 * scale_start

    scaling_time = 200
    widthUP = width_DOWN * scaleUP
    heightUP = height_DOWN * scaleUP
    w = width_DOWN
    h = height_DOWN
    w_karty = widthUP
    h_karty = heightUP
    dw = widthUP - width_DOWN
    dh = heightUP - height_DOWN

    #karta lezaca
    imgB_DOWN = pygame.image.load("textures/b0.png")
    imgB_DOWN = pygame.transform.scale_by(imgB_DOWN, scale_start)

    karta_przesuwana = pygame.transform.scale_by(imgB_DOWN, scaleUP)
    x = SCREEN_WIDTH/2 - widthUP/2
    moving_time = 400
    ds = widthUP + 20
    x_right = x + ds

    talia = imgB_DOWN


    liczba_graczy = 0
    karty_gracza = []
    karty_do_rozdania = 0

    

    wsp_graczy = []
    przedzial_na_gracza = SCREEN_WIDTH // (liczba_graczy-1)
    pierwszy_gracz = przedzial_na_gracza // 2 - width_DOWN // 2
    glowny_gracz = (SCREEN_WIDTH // 2 - width_DOWN // 2, SCREEN_HEIGHT - height_DOWN - 30)

    wsp_graczy.append(glowny_gracz)
    for i in range(1, liczba_graczy):
        wsp_graczy.append((pierwszy_gracz + (i-1) * przedzial_na_gracza, 30))

    rozdawana_karta = (0, 0)
    indeks_gracza = 0
    wsp_akt = (SCREEN_WIDTH/2 - width_DOWN/2, SCREEN_HEIGHT/2 - height_DOWN/2)
    v_karty = 1.5
    dx = 0
    dy = 0
    ile_rozdanych = -1

    #def klikniecie(x, y):
        
        
    #def puszczenie():
        

    #def ruch_myszki(x, y):
    def ustaw(dane):
        Rozdanie.czas_przejscia = 3000
        Rozdanie.liczba_graczy = len(dane.players)
        Rozdanie.karty_gracza = []
        Rozdanie.karty_do_rozdania = 0
        for i in dane.player_cards:
            Rozdanie.karty_gracza.append(len(i))
            Rozdanie.karty_do_rozdania += len(i)
        Rozdanie.wsp_graczy = []
        Rozdanie.przedzial_na_gracza = SCREEN_WIDTH // (Rozdanie.liczba_graczy-1)
        Rozdanie.pierwszy_gracz = Rozdanie.przedzial_na_gracza // 2 - Rozdanie.width_DOWN // 2
        Rozdanie.glowny_gracz = (SCREEN_WIDTH // 2 - Rozdanie.width_DOWN // 2, SCREEN_HEIGHT - Rozdanie.height_DOWN - 30)

        Rozdanie.wsp_graczy.append(Rozdanie.glowny_gracz)
        for i in range(1, Rozdanie.liczba_graczy):
            Rozdanie.wsp_graczy.append((Rozdanie.pierwszy_gracz + (i-1) * Rozdanie.przedzial_na_gracza, 30))

    def rysuj(screen, dt):
        screen.blit(Rozdanie.imgB_DOWN, (SCREEN_WIDTH/2 - Rozdanie.width_DOWN/2, SCREEN_HEIGHT/2 - Rozdanie.height_DOWN/2))

        Rozdanie.ile_rozdanych = min(Rozdanie.liczba_graczy-1, Rozdanie.ile_rozdanych)
        for i in range(Rozdanie.ile_rozdanych+1):
            screen.blit(Rozdanie.imgB_DOWN, Rozdanie.wsp_graczy[i])

        if Rozdanie.animacja_tasowania:
            if Rozdanie.zwiekszanie:
                Rozdanie.w += Rozdanie.dw*(dt/Rozdanie.scaling_time)
                Rozdanie.h += Rozdanie.dh*(dt/Rozdanie.scaling_time)
                if Rozdanie.w >= Rozdanie.widthUP:
                    Rozdanie.zwiekszanie = 0
                    Rozdanie.prawo = 1
                    Rozdanie.w = Rozdanie.widthUP
                    Rozdanie.h = Rozdanie.heightUP
                Rozdanie.talia = pygame.transform.rotozoom(Rozdanie.imgB_DOWN, 0, Rozdanie.w/Rozdanie.width_DOWN)
                screen.blit(Rozdanie.talia, (SCREEN_WIDTH/2 - Rozdanie.w/2, SCREEN_HEIGHT/2 - Rozdanie.h/2))
            elif Rozdanie.prawo:
                Rozdanie.x += Rozdanie.ds*(dt/Rozdanie.moving_time)
                if Rozdanie.x >= Rozdanie.x_right:
                    Rozdanie.prawo = 0
                    Rozdanie.zmniejszanie_tasowanej = 1
                    Rozdanie.x = Rozdanie.x_right
                screen.blit(Rozdanie.talia, (SCREEN_WIDTH/2 - Rozdanie.widthUP/2, SCREEN_HEIGHT/2 - Rozdanie.heightUP/2))
                screen.blit(Rozdanie.karta_przesuwana, (Rozdanie.x, SCREEN_HEIGHT/2 - Rozdanie.heightUP/2))
            elif Rozdanie.zmniejszanie_tasowanej:
                Rozdanie.w_karty -= Rozdanie.dw*(dt/Rozdanie.scaling_time)
                Rozdanie.h_karty -= Rozdanie.dh*(dt/Rozdanie.scaling_time)
                if Rozdanie.w_karty<= Rozdanie.width_DOWN:
                    Rozdanie.lewo = 1
                    Rozdanie.zmniejszanie_tasowanej = 0
                    Rozdanie.w_karty = Rozdanie.width_DOWN
                    Rozdanie.h_karty = Rozdanie.height_DOWN
                Rozdanie.karta_przesuwana = pygame.transform.rotozoom(Rozdanie.imgB_DOWN, 0, Rozdanie.w_karty/Rozdanie.width_DOWN)
                screen.blit(Rozdanie.karta_przesuwana, (Rozdanie.x_right+(Rozdanie.widthUP-Rozdanie.w_karty)/2, SCREEN_HEIGHT/2 - Rozdanie.h_karty/2))
                screen.blit(Rozdanie.talia, (SCREEN_WIDTH/2 - Rozdanie.widthUP/2, SCREEN_HEIGHT/2 - Rozdanie.heightUP/2))
            elif Rozdanie.lewo:
                screen.blit(Rozdanie.karta_przesuwana, (Rozdanie.x, SCREEN_HEIGHT/2 - Rozdanie.h_karty/2))
                screen.blit(Rozdanie.talia, (SCREEN_WIDTH/2 - Rozdanie.widthUP/2, SCREEN_HEIGHT/2 - Rozdanie.heightUP/2))
                Rozdanie.x -= Rozdanie.ds*(dt/Rozdanie.moving_time)
                if Rozdanie.x <= SCREEN_WIDTH/2 - Rozdanie.width_DOWN/2:
                    Rozdanie.lewo = 0
                    Rozdanie.prawo = 1
                    Rozdanie.x = SCREEN_WIDTH/2 - Rozdanie.width_DOWN/2
                    Rozdanie.kart_do_tasowania -= 1
                    Rozdanie.w_karty = Rozdanie.widthUP
                    Rozdanie.h_karty = Rozdanie.heightUP
                    Rozdanie.karta_przesuwana = Rozdanie.talia
                    if Rozdanie.kart_do_tasowania == 0:
                        Rozdanie.zmniejszanie = 1
                        Rozdanie.prawo = 0
                        Rozdanie.w = Rozdanie.widthUP
                        Rozdanie.h = Rozdanie.heightUP
            elif Rozdanie.zmniejszanie:
                Rozdanie.w -= Rozdanie.dw*(dt/Rozdanie.scaling_time)
                Rozdanie.h -= Rozdanie.dh*(dt/Rozdanie.scaling_time)
                if Rozdanie.w<= Rozdanie.width_DOWN:
                    Rozdanie.zwiekszanie = 1
                    Rozdanie.zmniejszanie = 0
                    Rozdanie.w = Rozdanie.width_DOWN
                    Rozdanie.h = Rozdanie.height_DOWN
                    Rozdanie.animacja_tasowania = 0
                    Rozdanie.animacja_rozdawania = 1
                    Rozdanie.kart_do_tasowania = 4
                Rozdanie.talia = pygame.transform.rotozoom(Rozdanie.imgB_DOWN, 0, Rozdanie.w/Rozdanie.width_DOWN)
                screen.blit(Rozdanie.talia, (SCREEN_WIDTH/2 - Rozdanie.w/2, SCREEN_HEIGHT/2 - Rozdanie.h/2))


        if Rozdanie.animacja_rozdawania:
            if Rozdanie.rozdawana_karta == (0, 0) and Rozdanie.karty_do_rozdania:
                print("rozdawanie")
                while Rozdanie.indeks_gracza < Rozdanie.liczba_graczy:
                    if Rozdanie.karty_gracza[Rozdanie.indeks_gracza]:
                        Rozdanie.rozdawana_karta = Rozdanie.wsp_graczy[Rozdanie.indeks_gracza]
                        Rozdanie.karty_gracza[Rozdanie.indeks_gracza] -= 1
                        Rozdanie.karty_do_rozdania -= 1
                        Rozdanie.indeks_gracza += 1
                        if Rozdanie.indeks_gracza == Rozdanie.liczba_graczy:
                            Rozdanie.indeks_gracza = 0
                        Rozdanie.wsp_akt = (SCREEN_WIDTH/2 - Rozdanie.width_DOWN/2, SCREEN_HEIGHT/2 - Rozdanie.height_DOWN/2)
                        Rozdanie.dx = (Rozdanie.rozdawana_karta[0] - Rozdanie.wsp_akt[0])
                        Rozdanie.dy = (Rozdanie.rozdawana_karta[1] - Rozdanie.wsp_akt[1])
                        print(Rozdanie.indeks_gracza)
                        break
            elif Rozdanie.rozdawana_karta == (0, 0) and Rozdanie.karty_do_rozdania == 0:
                Rozdanie.animacja_rozdawania = 0
            else:
                #print(Rozdanie.rozdawana_karta)
                droga = (Rozdanie.dx**2 + Rozdanie.dy**2)**0.5
                przbyta = dt*Rozdanie.v_karty/droga
                wsp_x = Rozdanie.dx*przbyta
                wsp_y = Rozdanie.dy*przbyta 
                wsp_x += Rozdanie.wsp_akt[0]
                wsp_y += Rozdanie.wsp_akt[1]
                Rozdanie.wsp_akt = (wsp_x, wsp_y)
                if ((Rozdanie.dx >= 0 and Rozdanie.wsp_akt[0] >= Rozdanie.rozdawana_karta[0]) or (Rozdanie.dx < 0 and Rozdanie.wsp_akt[0] <= Rozdanie.rozdawana_karta[0])) and ((Rozdanie.dy >= 0 and Rozdanie.wsp_akt[1] >= Rozdanie.rozdawana_karta[1]) or (Rozdanie.dy < 0 and Rozdanie.wsp_akt[1] <= Rozdanie.rozdawana_karta[1])):
                    Rozdanie.wsp_akt = (Rozdanie.rozdawana_karta[0], Rozdanie.rozdawana_karta[1])
                    Rozdanie.rozdawana_karta = (0, 0)
                    Rozdanie.ile_rozdanych += 1
                screen.blit(Rozdanie.imgB_DOWN, Rozdanie.wsp_akt)


        if Rozdanie.animacja_tasowania == 0 and Rozdanie.animacja_rozdawania == 0:
            Rozdanie.czas_przejscia -=dt
