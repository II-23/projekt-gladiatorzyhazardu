import pygame
from zmienne import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

liczba_kart = 3
zwiekszanie = 1
zmniejszanie = 0
zmniejszanie_tasowanej = 0
prawo = 0
lewo = 0
kart_do_tasowania = 4
animacja_tasowania = 1

scaleUP = 1.1
scale_start = 0.15
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
moving_time = 600
ds = widthUP + 20
x_right = x + ds

talia = imgB_DOWN

while True:
    dt = clock.tick(30)
    bg = pygame.image.load("data/images/kolor.png")
    screen.blit(bg, (0, 0))
    screen.blit(imgB_DOWN, (SCREEN_WIDTH/2 - width_DOWN/2, SCREEN_HEIGHT/2 - height_DOWN/2))

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
                kart_do_tasowania = 4
            talia = pygame.transform.rotozoom(imgB_DOWN, 0, w/width_DOWN)
            screen.blit(talia, (SCREEN_WIDTH/2 - w/2, SCREEN_HEIGHT/2 - h/2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.display.update()
