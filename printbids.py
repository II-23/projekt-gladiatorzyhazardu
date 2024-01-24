import pygame
from zmienne import *
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
RECTANGLE_WIDTH, RECTANGLE_HEIGHT = 312, 75
MARGIN = 2
BACKGROUND_COLOR = (200, 200, 200)
RECTANGLE_COLOR = (100, 100, 255)
TEXT_COLOR = (0, 0, 0)



font = pygame.font.SysFont("comicsansms",round(30*SCALE)) #font to be set



#use with different opacity to represent new bid apperance
def display_new_bids(screen, strings, nicks,opacity, start_pos=(16,40), scale=1.0):
    if len(strings) == 0: 
        return
    print(strings)
    strings=strings[::-1]
    strings = strings[:min(len(strings),8)]
    nicks=nicks[::-1]
    nicks =nicks[:min(len(nicks),8)]

    shape_img = pygame.image.load("textures/shape.png")
    shape_img = pygame.transform.scale(shape_img, (RECTANGLE_WIDTH * scale, RECTANGLE_HEIGHT * scale))
    shape = shape_img.get_rect()

    shape_img.set_alpha(opacity)
    text = font.render(nicks[0]+" : " + strings[0], True, TEXT_COLOR)
    text.set_alpha(opacity)

    shape.topleft = (start_pos[0], start_pos[1])
    text_rect = text.get_rect(center=shape.center)
    
    screen.blit(shape_img, shape)
    screen.blit(text, text_rect)

    shape_img.set_alpha(255)
    text.set_alpha(255)
    y_position = start_pos[1] + RECTANGLE_HEIGHT * scale + 2 * MARGIN * scale

    for i in range(1,len(strings)):
        text = font.render(nicks[i]+" : " + strings[i], True, TEXT_COLOR)
        shape.topleft = (start_pos[0], y_position)
        text_rect = text.get_rect(center=shape.center)

        screen.blit(shape_img,shape)
        screen.blit(text, text_rect)

        y_position += RECTANGLE_HEIGHT * scale + 2 * MARGIN * scale

# \/\/\/\/\/\/testowanie\/\/\/\/\/\/\/\
# Example list of strings 
# string_list = ["Hello", "Pygame", "String", "Visualization", "List", "Trzy dziewiątki dwie dziesiatki","Wysoka Król","sex","Kopor Krolewski","asda","Piotr Wawrzyniak","Trzy dziewiątki dwie dziesiatki"]
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("String Visualization")
# bg=pygame.image.load("ground.png")
# bg=pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
# wsk=-1
# screen.blit(bg,(0,0))
# pygame.display.flip()
# while True:
#     screen.blit(bg,(0,0))
#     # display_new_bids(string_list)
#     if wsk<len(string_list):
#         wsk+=1
#         display_new_bids(screen,string_list[:wsk])
#         time.sleep(0.5)
#     else:   display_bids(screen,string_list[:wsk])
    
#     # display_new_bids(string_list)
#     time.sleep(1/30)

