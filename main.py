import pygame
import sys


pygame.init()
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Poker tajski")
clock = pygame.time.Clock()


#kolory
grey=(220,220,220)
dark_grey=(180, 180, 180)
red=(255,160,122)
dark_red=(255,120,80)
black=(0, 0, 0)

# Rysowanie tła
def rysuj_tlo():
    bg = pygame.image.load("data/images/kolor.png")
    screen.blit(bg, (0, 0))

class Menu:
    stan=0

    #menu
    glowny=(50, 50, screen_width-100, screen_height-100)
    

    #tytuł
    font=pygame.font.SysFont("comicsansms", 120)
    tytul = font.render("Poker tajski", True, dark_red)
    
    #Start
    font = pygame.font.SysFont("comicsansms", 100)
    start_napis = font.render("Start", True, dark_red)
    start_corner=(screen_width//2 - start_napis.get_width() // 2, 1.75*screen_height//5 - start_napis.get_height() // 2)
    start_button=(start_corner[0]-25, start_corner[1]-10, start_napis.get_width()+50, start_napis.get_height()+20)
    
    

    #jak grac
    font = pygame.font.SysFont("comicsansms", 80)
    htp_napis = font.render("Jak grać", True, dark_red)
    htp_corner=(screen_width//2 - htp_napis.get_width() // 2, 2.5*screen_height//5 - htp_napis.get_height() // 2)
    htp_button=(htp_corner[0]-25, htp_corner[1]-10, htp_napis.get_width()+50, htp_napis.get_height()+20)
    

    def klikniecie(x, y):
        if x>=Menu.start_corner[0]-25 and x<=Menu.start_corner[0]+Menu.start_napis.get_width()+50 and y>=Menu.start_corner[1]-10 and y<=Menu.start_corner[1]+Menu.start_napis.get_height()+30:
            return 1
        return Menu.stan
        
    def rysuj():
        pygame.draw.rect(screen, grey, Menu.glowny)
        screen.blit(Menu.tytul, (screen_width//2 - Menu.tytul.get_width() // 2, screen_height//5 - Menu.tytul.get_height() // 2))

        pygame.draw.rect(screen, dark_grey, Menu.start_button)
        pygame.draw.rect(screen, black, Menu.start_button, 5)
        screen.blit(Menu.start_napis, Menu.start_corner)

        pygame.draw.rect(screen, dark_grey, Menu.htp_button)
        pygame.draw.rect(screen, black, Menu.htp_button, 5)
        screen.blit(Menu.htp_napis, Menu.htp_corner)

        #pygame.draw.rect(screen, black, (100, 50, 25, 25))

class preGame:
    stan=1

        

class Gra:
    liczba_graczy=4
    stan_gry=Menu.stan

    def cofnij_stan():
        if Gra.stan_gry==preGame.stan:
            Gra.stan_gry=Menu.stan
    

while True:
    clock.tick(60)
    rysuj_tlo()
    mouse = pygame.mouse.get_pos() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Gra.stan_gry==Menu.stan:
                Gra.stan_gry=Menu.klikniecie(mouse[0], mouse[1]) 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Gra.cofnij_stan()

    if Gra.stan_gry==Menu.stan:
        Menu.rysuj()
    #if Gra.stan_gry==preGame.stan:


                

    
    pygame.display.update()