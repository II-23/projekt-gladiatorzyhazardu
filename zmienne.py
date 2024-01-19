import pygame
import tkinter
import screeninfo

root = tkinter.Tk()


pygame.init()
# SCREEN_WIDTH = 1920
# SCREEN_HEIGHT = 1080
# TABLE_WIDTH = 1593 - 342
# TABLE_HEIGHT = 1061 - 18
# TABLE_CORNER = (343, 19)
# TABLE_CENTER = (TABLE_CORNER[0] + TABLE_WIDTH/2, TABLE_CORNER[1] + TABLE_HEIGHT/2)

SCREEN = screeninfo.get_monitors()[0]
SCREEN_WIDTH = SCREEN.width
SCREEN_HEIGHT = SCREEN.height
TABLE_WIDTH = 1593 - 342
TABLE_WIDTH = int(TABLE_WIDTH * SCREEN_WIDTH / 1920)
TABLE_HEIGHT = 1061 - 18
TABLE_HEIGHT = int(TABLE_HEIGHT * SCREEN_HEIGHT / 1080)
TABLE_CORNER = (343, 19)
TABLE_CORNER = (int(TABLE_CORNER[0] * SCREEN_WIDTH / 1920), int(TABLE_CORNER[1] * SCREEN_HEIGHT / 1080))
TABLE_CENTER = (TABLE_CORNER[0] + TABLE_WIDTH/2, TABLE_CORNER[1] + TABLE_HEIGHT/2)


# kolory
GREY = (220, 220, 220)
DARK_GREY = (180, 180, 180)
RED = (255, 160, 122)
DARK_RED = (255, 120, 80)
BLACK = (0, 0, 0)


#dane
#PLAYERS = c
AKCJA = 11