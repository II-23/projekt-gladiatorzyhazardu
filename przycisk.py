import pygame
from zmienne import SCALE
BUTTON_X = 1630*SCALE
BUTTON_START_Y = 100 *SCALE
BUTTON_WIDTH = 255*SCALE
BUTTON_HEIGHT = 55*SCALE

background_color = (48, 90, 74, 255)
kolor_przycisku1 = (255, 255, 255)
kolor_przycisku2 = (161, 221, 186)
kolor_przycisku3 = (217, 242, 228)
kolor_przycisku4 = (255, 0, 255) # <- do zmiany (kolor kliknietego przycisku)

ramka_color = (0, 0, 0)

class Przycisk:
    def __init__(self, x, y, width, height, text, sub_buttons=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.sub_buttons = sub_buttons or []
        self.color = kolor_przycisku1

        if sub_buttons == None:
            self.color = kolor_przycisku3

        self.expanded = False
        self.visible = True
        self.unlocked = True

    def draw(self, screen: pygame.Surface, is_clicked=False, is_legal=True):

        if is_legal == False:
            rect_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            pygame.draw.rect(rect_surface, self.color + (128,), rect_surface.get_rect(), border_radius=10)
            screen.blit(rect_surface, (self.rect.x, self.rect.y))
        elif is_clicked:
            pygame.draw.rect(screen, kolor_przycisku4, self.rect, border_radius=10)
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        pygame.draw.rect(screen, ramka_color, self.rect, 1, border_radius=6)                  #ramka
        if self.sub_buttons:
            font = pygame.font.Font(None, round(28*SCALE))
        else:
            font = pygame.font.Font(None, round(24*SCALE))
        
        text = font.render(self.text, True, (0, 0, 0))
        
        if is_legal == False:
            text.set_alpha(128)

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
            if self.rect.collidepoint(event.pos) and self.visible:
                self.toggle_expanded()
                print (self.text)
                return self.text
        return None

    def toggle_expanded(self):
        self.expanded = not self.expanded