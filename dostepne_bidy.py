
#na razie tylko rysuje rozwijane nieladne przyciski jak debil

import pygame
from zmienne import *
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption('lista bidow')


background_color = (48, 90, 74, 255)

kolor_przycisku1 = (0, 128, 255)
kolor_przycisku2 = (0, 255, 128)


class przycisk:
    def __init__(self, x, y, width, height, text, sub_buttons=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.sub_buttons = sub_buttons or []
        self.expanded = False
        self.color = kolor_przycisku1

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = kolor_przycisku2
            else:
                self.color = kolor_przycisku1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.toggle_expanded()

    def toggle_expanded(self):
        self.expanded = not self.expanded




def opcje(i, y):
    uklady = [[],[],[]]
    uklady[0] = [przycisk(100, y+50, 150, 50, "Nine"), 
                 przycisk(100, y+100, 150, 50, "Ten"), 
                 przycisk(100, y+150, 150, 50, "Jack"), 
                 przycisk(100, y+200, 150, 50, "Queen"), 
                 przycisk(100, y+250, 150, 50, "King"), 
                 przycisk(100, y+300, 150, 50, "Ace")
                 ]
    uklady[1] = [przycisk(100, y+50, 150, 50, "Low"),
                 przycisk(100, y+100, 150, 50, "High")
                 ]
    uklady[2] = [przycisk(100, y+50, 150, 50, "Clubs"), 
                 przycisk(100, y+100, 150, 50, "Diamonds"),
                 przycisk(100, y+150, 150, 50, "Hearts"),
                 przycisk(100, y+200, 150, 50, "Spades")
                 ]
    return uklady[i]



buttons = [                      # trzeba zmienic im wspolrzedne by zaczynaly sie rysowac od gory dopiero te dostepne

    przycisk(100, 100, 200, 50, "High", opcje(0, 100)),      #figura
    przycisk(100, 200, 200, 50, "Pair", opcje(0, 200)),      
    przycisk(100, 300, 200, 50, "Straight", opcje(1, 300)),   #strit duzy maly
    przycisk(100, 400, 200, 50, "Three", opcje(0, 400)),
    przycisk(100, 500, 200, 50, "Full", opcje(0, 500)),    #naprawic!!!  brakuje wyboru dwoch
    przycisk(100, 600, 200, 50, "Flush", opcje(2, 600)),    #kolor
    przycisk(100, 700, 200, 50, "Four", opcje(0, 700)),
    przycisk(100, 800, 200, 50, "Poker", opcje(2, 800)),           #kolor
    przycisk(100, 900, 200, 50, "King poker", opcje(2, 900))        
]


def narysuj_przyciski (buttons, last_bid):           # zeby byly dostepne bidy
    for button in buttons:
        button.draw()
    for button in buttons:    #musza byc osobne fory by nie rysowaly sie pod spodem!
        if button.expanded:
            for sub_button in button.sub_buttons:
                sub_button.draw()



last_bid = 0            # trzeba dostac tego bida
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for button in buttons:
            button.handle_event(event)
            if button.expanded:
                for sub_button in button.sub_buttons:
                    sub_button.handle_event(event)

    screen.fill(background_color)

    narysuj_przyciski(buttons, last_bid)         # bo nie bedzei rysowal wszystkich
    
    pygame.display.flip()
