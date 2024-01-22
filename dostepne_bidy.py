#1
#na razie wyswietlaja sie wszystkie bidy a nie tylko dozwolone
#tak samo mozna deklarowac wszystkie bidy
#do dokonczenia komunikacja z serwerem
# w zaleznosci od tego w jakiej formie client przyjmuje/zwraca bidy

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
from przycisk import *

def opcje(i, y, key):
    bid = bids[key]
    uklady = []
    if key != 'full house':
        for j, (key2, bid2) in enumerate (bid.items()):
            sbt = Przycisk(BUTTON_X, y + BUTTON_HEIGHT * (j+1), BUTTON_WIDTH, BUTTON_HEIGHT, key2)
            uklady.append(sbt)
    else:
        for j in range(6):
            sbt = Przycisk(BUTTON_X, y + BUTTON_HEIGHT * (j+1), BUTTON_WIDTH/2, BUTTON_HEIGHT, 'full '+Figures[j+9])
            uklady.append(sbt)
        for j in range(6):
            sbt = Przycisk(BUTTON_X + BUTTON_WIDTH/2, y + BUTTON_HEIGHT * (j+1), BUTTON_WIDTH/2, BUTTON_HEIGHT, ' on '+Figures[j+9])
            uklady.append(sbt)
    return uklady

last_clicked_index = -1
clicked = None
clicked_bid = None
clicked_bid2 = None

make_bid_button = Przycisk(BUTTON_X, BUTTON_START_Y+14*BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT*2, 'MAKE BID')
buttons = []
for i, (key, bid) in enumerate (bids.items()):
    bt = Przycisk(BUTTON_X, BUTTON_START_Y + i * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, key, opcje(i, BUTTON_START_Y + i * BUTTON_HEIGHT, key))
    buttons.append(bt)


def draw_buttons(screen, last_bid):
    pole = pygame.Rect((BUTTON_X-2, BUTTON_START_Y, BUTTON_WIDTH+4, BUTTON_HEIGHT*16+4))
    pygame.draw.rect(screen, kolor_przycisku1, pole, border_radius=10)
    pygame.draw.rect(screen, ramka_color, pole, 2, border_radius=10)

    for button in buttons:
        if button.visible:
            button.draw(screen)
    
    is_legal = False

    if last_bid == None:
        is_legal = True
    
    for button in buttons:
        for sub_button in button.sub_buttons:
            if last_bid != None and \
                sub_button.text in last_bid and \
                'full ' in sub_button.text and \
                'on ace' not in last_bid:
                is_legal = True

            if button.expanded:
                if sub_button.text == clicked_bid:
                    sub_button.draw(screen, True, is_legal)
                elif 'on ' in sub_button.text:
                    if clicked_bid == None or last_bid == None:
                        sub_button.draw(screen, sub_button.text == clicked_bid2, is_legal)
                    else:
                        is_full_legal = compare_bids(clicked_bid + sub_button.text, last_bid)

                        # print("CLICKED: ", f"'{clicked_bid + sub_button.text}' vs {last_bid}", is_full_legal)

                        if sub_button.text == clicked_bid2:
                            sub_button.draw(screen, True, is_full_legal)
                        else:
                            sub_button.draw(screen, False, is_full_legal)
                else:
                    sub_button.draw(screen, False, is_legal)

            if last_bid != None and \
                sub_button.text in last_bid:
                is_legal = True
    
    make_bid_button.draw(screen)

def handle_button_event(event):

    global last_clicked_index
    global clicked
    global clicked_bid
    global clicked_bid2

    # print("> ", last_clicked_index, f"'{clicked}'", f"'{clicked_bid}'", f"'{clicked_bid2}'")

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
                clicked = button.text

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
                tmp = sub_button.handle_event(event)
                if clicked and tmp:
                    if clicked != 'full house':
                        clicked_bid = tmp
                    else:
                        if 'full' in tmp:
                            clicked_bid = tmp
                        elif 'on' in tmp:
                            clicked_bid2 = tmp

        
        #make bid
        if event.type == pygame.MOUSEMOTION:
            if make_bid_button.rect.collidepoint(event.pos):
                make_bid_button.color = kolor_przycisku2
            else:
                make_bid_button.color = kolor_przycisku1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if make_bid_button.rect.collidepoint(event.pos):
                if clicked == 'full house' and (not clicked_bid or not clicked_bid2) :
                    continue
                elif clicked == 'full house' and clicked_bid + clicked_bid2 not in bids['full house']:
                    continue
                elif clicked == 'full house': 
                    clicked_bid += clicked_bid2
                
                #komunikacja z serwerem
                #MakeBid(dane, clicked, clicked_bid)
                #na razie dla fulla nie działa
                
                # print("CLICKED: " , clicked_bid)
                return clicked_bid
    return None