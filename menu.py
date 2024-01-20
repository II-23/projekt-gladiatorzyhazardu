import pygame
from zmienne import *

class Menu:
    stan = 0

    # menu
    # Start
    start_texture = pygame.image.load("textures/button-start.png")
    start_texture = pygame.transform.scale(start_texture, (round(start_texture.get_width() *SCALE), round(start_texture.get_height() *SCALE)))  
    start_texture_re=start_texture.get_rect(center=(SCREEN_WIDTH//2-10*SCALE,SCREEN_HEIGHT//2))


    def klikniecie(x, y):
        if Menu.start_texture_re.collidepoint((x,y)):
            return 1
        return Menu.stan

    def rysuj(screen):        
        screen.blit(Menu.start_texture, Menu.start_texture_re)

