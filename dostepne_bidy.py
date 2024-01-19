import pygame
from zmienne import *
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.SCALED|pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption('lista bidow')


background_color = (48, 90, 74, 255)
kolor_przycisku1 = (255, 255, 255)
kolor_przycisku2 = (161, 221, 186)
kolor_przycisku3 = (217, 242, 228)
ramka_color = (0, 0, 0)

class przycisk:
    def __init__(self, x, y, width, height, text, sub_buttons=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.sub_buttons = sub_buttons or []
        self.expanded = False
        self.color = kolor_przycisku1
        if sub_buttons == None:
            self.color = kolor_przycisku3
        self.visible = True
        self.unlocked = True

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)     #zaokraglone rogi
        pygame.draw.rect(screen, ramka_color, self.rect, 1, border_radius=6)                  #ramka
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = kolor_przycisku2
            else:
                if self.sub_buttons:
                    self.color = kolor_przycisku1
                else:
                    self.color = kolor_przycisku3
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):# and self.visible:
                self.toggle_expanded()

    def toggle_expanded(self):
        self.expanded = not self.expanded




def opcje(i, y):
    uklady = [[],[],[],[]]
    uklady[0] = [przycisk(1600, y+50, 200, 50, "nine"),
                 przycisk(1600, y+100, 200, 50, "ten"),
                 przycisk(1600, y+150, 200, 50, "jack"),
                 przycisk(1600, y+200, 200, 50, "queen"),
                 przycisk(1600, y+250, 200, 50, "king"),
                 przycisk(1600, y+300, 200, 50, "ace")
                 ]
    uklady[1] = [przycisk(1600, y+50, 200, 50, "low"),
                 przycisk(1600, y+100, 200, 50, "high")
                 ]
    uklady[2] = [przycisk(1600, y+50, 200, 50, "clubs"),
                 przycisk(1600, y+100, 200, 50, "diamonds"),
                 przycisk(1600, y+150, 200, 50, "hearts"),
                 przycisk(1600, y+200, 200, 50, "spades")
                 ]
    uklady[3] = [przycisk(1600, y+50, 100, 50, "nine"),        #full
                 przycisk(1600, y+100, 100, 50, "ten"),
                 przycisk(1600, y+150, 100, 50, "jack"),
                 przycisk(1600, y+200, 100, 50, "queen"),
                 przycisk(1600, y+250, 100, 50, "king"),
                 przycisk(1600, y+300, 100, 50, "ace"),

                 przycisk(1700, y+50, 100, 50, "nine"),
                 przycisk(1700, y+100, 100, 50, "ten"),
                 przycisk(1700, y+150, 100, 50, "jack"),
                 przycisk(1700, y+200, 100, 50, "queen"),
                 przycisk(1700, y+250, 100, 50, "king"),
                 przycisk(1700, y+300, 100, 50, "ace")
                 ]

    return uklady[i]


buttons = [                      # trzeba zmienic im wspolrzedne by zaczynaly sie rysowac od gory dopiero te dostepne
    przycisk(1600, 100, 200, 50, "high", opcje(0, 100)),      #figura
    przycisk(1600, 150, 200, 50, "pair", opcje(0, 150)),
    przycisk(1600, 200, 200, 50, "straight", opcje(1, 200)),   #strit duzy maly
    przycisk(1600, 250, 200, 50, "three", opcje(0, 250)),
    przycisk(1600, 300, 200, 50, "full", opcje(3, 300)),
    przycisk(1600, 350, 200, 50, "flush", opcje(2, 350)),    #kolor
    przycisk(1600, 400, 200, 50, "four", opcje(0, 400)),
    przycisk(1600, 450, 200, 50, "poker", opcje(2, 450)),    #kolor
    przycisk(1600, 500, 200, 50, "king poker", opcje(2, 500))
]


def narysuj_przyciski (buttons, last_bid):           # zeby byly dostepne bidy
    pole = pygame.Rect((1598, 98, 204, 804))
    pygame.draw.rect(screen, kolor_przycisku1, pole, border_radius=10)     #zaokraglone rogi
    pygame.draw.rect(screen, ramka_color, pole, 2, border_radius=10)                  #ramka
    for button in buttons:
        if button.visible:
            button.draw()
    for button in buttons:    #musza byc osobne fory by nie rysowaly sie pod spodem!
        if button.expanded:
            for sub_button in button.sub_buttons:
                sub_button.draw()





last_bid = 0            # trzeba dostac tego bida
last_clicked_index = None

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for i, button in enumerate(buttons):

            #poczatek button.handle_event(event)
            if event.type == pygame.MOUSEMOTION:
                if button.rect.collidepoint(event.pos):
                    button.color = kolor_przycisku2
                else:
                    button.color = kolor_przycisku1

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos) and button.visible and button.unlocked:
                    button.toggle_expanded()

                    if last_clicked_index == i:         #przywracam dla tego samego przycisku
                        for j in range(i + 1, len(buttons)):
                            buttons[j].visible = True
                        for j in range(len(buttons)):
                            buttons[j].unlocked = True
                        last_clicked_index = None
                    else:                               #ukrywam przyciski
                        for j in range(i + 1, len(buttons)):
                            buttons[j].visible = False
                        for j in range(len(buttons)):
                            buttons[j].unlocked = False
                        button.visible = True
                        button.unlocked = True
                        last_clicked_index = i

            ##koniec button.handle_event(event)
            if button.expanded:
                for sub_button in button.sub_buttons:
                    sub_button.handle_event(event)

    screen.fill(background_color)

    narysuj_przyciski(buttons, last_bid)         # bo nie bedzei rysowal wszystkich

    pygame.display.flip()
    clock.tick(60) 