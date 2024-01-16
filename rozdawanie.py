import pygame
from zmienne import *
import sys
from pygame.locals import *

pygame.init()
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
clock = pygame.time.Clock()

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


liczba_graczy = 5
karty_gracza = []
karty_do_rozdania = 0

for i in range(liczba_graczy):
    karty_gracza.append(4)
    karty_do_rozdania += 4

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
while True:
    dt = clock.tick(30)
    bg = pygame.image.load("data/images/kolor.png")
    screen.blit(bg, (0, 0))
    screen.blit(imgB_DOWN, (SCREEN_WIDTH/2 - width_DOWN/2, SCREEN_HEIGHT/2 - height_DOWN/2))

    ile_rozdanych = min(liczba_graczy-1, ile_rozdanych)
    for i in range(ile_rozdanych+1):
        screen.blit(imgB_DOWN, wsp_graczy[i])

    if animacja_tasowania:
        if zwiekszanie:
            w += dw*(dt/scaling_time)
            h += dh*(dt/scaling_time)
            if w >= widthUP:
                zwiekszanie = 0
                prawo = 1
                w = widthUP
                h = heightUP
            talia = pygame.transform.rotozoom(imgB_DOWN, 0, w/width_DOWN)
            screen.blit(talia, (SCREEN_WIDTH/2 - w/2, SCREEN_HEIGHT/2 - h/2))
        elif prawo:
            x += ds*(dt/moving_time)
            if x >= x_right:
                prawo = 0
                zmniejszanie_tasowanej = 1
                x = x_right
            screen.blit(talia, (SCREEN_WIDTH/2 - widthUP/2, SCREEN_HEIGHT/2 - heightUP/2))
            screen.blit(karta_przesuwana, (x, SCREEN_HEIGHT/2 - heightUP/2))
        elif zmniejszanie_tasowanej:
            w_karty -= dw*(dt/scaling_time)
            h_karty -= dh*(dt/scaling_time)
            if w_karty<= width_DOWN:
                lewo = 1
                zmniejszanie_tasowanej = 0
                w_karty = width_DOWN
                h_karty = height_DOWN
            karta_przesuwana = pygame.transform.rotozoom(imgB_DOWN, 0, w_karty/width_DOWN)
            screen.blit(karta_przesuwana, (x_right+(widthUP-w_karty)/2, SCREEN_HEIGHT/2 - h_karty/2))
            screen.blit(talia, (SCREEN_WIDTH/2 - widthUP/2, SCREEN_HEIGHT/2 - heightUP/2))
        elif lewo:
            screen.blit(karta_przesuwana, (x, SCREEN_HEIGHT/2 - h_karty/2))
            screen.blit(talia, (SCREEN_WIDTH/2 - widthUP/2, SCREEN_HEIGHT/2 - heightUP/2))
            x -= ds*(dt/moving_time)
            if x <= SCREEN_WIDTH/2 - width_DOWN/2:
                lewo = 0
                prawo = 1
                x = SCREEN_WIDTH/2 - width_DOWN/2
                kart_do_tasowania -= 1
                w_karty = widthUP
                h_karty = heightUP
                karta_przesuwana = talia
                if kart_do_tasowania == 0:
                    zmniejszanie = 1
                    prawo = 0
                    w = widthUP
                    h = heightUP
        elif zmniejszanie:
            w -= dw*(dt/scaling_time)
            h -= dh*(dt/scaling_time)
            if w<= width_DOWN:
                zwiekszanie = 1
                zmniejszanie = 0
                w = width_DOWN
                h = height_DOWN
                animacja_tasowania = 0
                animacja_rozdawania = 1
                kart_do_tasowania = 4
            talia = pygame.transform.rotozoom(imgB_DOWN, 0, w/width_DOWN)
            screen.blit(talia, (SCREEN_WIDTH/2 - w/2, SCREEN_HEIGHT/2 - h/2))


    if animacja_rozdawania:
        if rozdawana_karta == (0, 0) and karty_do_rozdania:
            #print("rozdawanie")
            while indeks_gracza < liczba_graczy:
                if karty_gracza[indeks_gracza]:
                    rozdawana_karta = wsp_graczy[indeks_gracza]
                    karty_gracza[indeks_gracza] -= 1
                    karty_do_rozdania -= 1
                    indeks_gracza += 1
                    if indeks_gracza == liczba_graczy:
                        indeks_gracza = 0
                    wsp_akt = (SCREEN_WIDTH/2 - width_DOWN/2, SCREEN_HEIGHT/2 - height_DOWN/2)
                    dx = (rozdawana_karta[0] - wsp_akt[0])
                    dy = (rozdawana_karta[1] - wsp_akt[1])
                    print(indeks_gracza)
                    break
        elif rozdawana_karta == (0, 0) and karty_do_rozdania == 0:
            animacja_rozdawania = 0
        else:
            print(rozdawana_karta)
            droga = (dx**2 + dy**2)**0.5
            przbyta = dt*v_karty/droga
            wsp_x = dx*przbyta
            wsp_y = dy*przbyta 
            wsp_x += wsp_akt[0]
            wsp_y += wsp_akt[1]
            wsp_akt = (wsp_x, wsp_y)
            if ((dx >= 0 and wsp_akt[0] >= rozdawana_karta[0]) or (dx < 0 and wsp_akt[0] <= rozdawana_karta[0])) and ((dy >= 0 and wsp_akt[1] >= rozdawana_karta[1]) or (dy < 0 and wsp_akt[1] <= rozdawana_karta[1])):
                wsp_akt = (rozdawana_karta[0], rozdawana_karta[1])
                rozdawana_karta = (0, 0)
                ile_rozdanych += 1
            screen.blit(imgB_DOWN, wsp_akt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.display.update()
