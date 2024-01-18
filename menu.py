import pygame
from zmienne import *

class Menu:
    stan = 0

    # menu
    # tytuł
    font = pygame.font.SysFont("comicsansms", 120)
    tytul = font.render("Poker tajski", True, DARK_RED)

    # Start
    start_texture = pygame.image.load("textures/button-start.png")
    start_texture = pygame.transform.scale(start_texture, (start_texture.get_width() // 2, start_texture.get_height() // 1.8))  
    start_corner = (
        SCREEN_WIDTH // 2 - start_texture.get_width() // 2,
        1.75 * SCREEN_HEIGHT // 5 - start_texture.get_height() // 2,
    )
    start_button = (
        start_corner[0] - 25,
        start_corner[1] - 10,
        start_texture.get_width() + 50,
        start_texture.get_height() + 20,
    )

    # jak grac
    font = pygame.font.SysFont("comicsansms", 80)
    htp_napis = font.render("Jak grać", True, DARK_RED)
    htp_corner = (
        SCREEN_WIDTH // 2 - htp_napis.get_width() // 2,
        2.5 * SCREEN_HEIGHT // 5 - htp_napis.get_height() // 2,
    )
    htp_button = (
        htp_corner[0] - 25,
        htp_corner[1] - 10,
        htp_napis.get_width() + 50,
        htp_napis.get_height() + 20,
    )

    def klikniecie(x, y):
        if (
            x >= Menu.start_corner[0] - 25
            and x <= Menu.start_corner[0] + Menu.start_texture.get_width() + 50
            and y >= Menu.start_corner[1] - 10
            and y <= Menu.start_corner[1] + Menu.start_texture.get_height() + 30
            ):
            return 1
        return Menu.stan

    def rysuj(screen):
        screen.blit(
            Menu.tytul,
            (
                SCREEN_WIDTH // 2 - Menu.tytul.get_width() // 2,
                SCREEN_HEIGHT // 5 - Menu.tytul.get_height() // 2,
            ),
        )

        
        screen.blit(Menu.start_texture, Menu.start_corner)

        pygame.draw.rect(screen, DARK_GREY, Menu.htp_button)
        pygame.draw.rect(screen, BLACK, Menu.htp_button, 5)
        screen.blit(Menu.htp_napis, Menu.htp_corner)

