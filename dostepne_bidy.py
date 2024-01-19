import pygame
import sys
from client import client
from zmienne import *
from menu import *
from pregame import *
from rozgrywka import *
from rozdanie import *
from info_o_grze import *
from pygame.locals import *
from logic.bids import *
from logic.cards import *

dane = game_info()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption('lista bidow')

BUTTON_X = 1600
BUTTON_START_Y = 100
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 50


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
        if self.sub_buttons:
            font = pygame.font.Font(None, 28)
        else:
            font = pygame.font.Font(None, 22)
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




def opcje(i, y, key):
    bid = bids[key]
    uklady = []
    if key != 'full house':
        for j, (key2, bid2) in enumerate (bid.items()):
            sbt = przycisk (BUTTON_X, y + BUTTON_HEIGHT * (j+1), BUTTON_WIDTH, BUTTON_HEIGHT, key2)
            uklady.append(sbt)
    else:
        for j in range(6):
            sbt = przycisk (BUTTON_X, y + BUTTON_HEIGHT * (j+1), BUTTON_WIDTH/2, BUTTON_HEIGHT, 'full house '+Figures[j+9])
            uklady.append(sbt)
        for j in range(6):
            sbt = przycisk (BUTTON_X + BUTTON_WIDTH/2, y + BUTTON_HEIGHT * (j+1), BUTTON_WIDTH/2, BUTTON_HEIGHT, ' on '+Figures[j+9])
            uklady.append(sbt)
    return uklady


buttons = []
for i, (key, bid) in enumerate (bids.items()):
    bt = przycisk(BUTTON_X, BUTTON_START_Y + i * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, key, opcje(i, BUTTON_START_Y + i * BUTTON_HEIGHT, key))
    buttons.append(bt)





def narysuj_przyciski (buttons, last_bid):           # zeby byly dostepne bidy
    pole = pygame.Rect((BUTTON_X-2, BUTTON_START_Y, BUTTON_WIDTH+4, BUTTON_HEIGHT*16+4))
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