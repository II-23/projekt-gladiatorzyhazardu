import pygame

BUTTON_X = 1600
BUTTON_START_Y = 100
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 50

background_color = (48, 90, 74, 255)
kolor_przycisku1 = (255, 255, 255)
kolor_przycisku2 = (161, 221, 186)
kolor_przycisku3 = (217, 242, 228)
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

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)     #zaokraglone rogi
        pygame.draw.rect(screen, ramka_color, self.rect, 1, border_radius=6)                  #ramka
        if self.sub_buttons:
            font = pygame.font.Font(None, 28)
        else:
            font = pygame.font.Font(None, 24)
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
            if self.rect.collidepoint(event.pos) and self.visible:
                self.toggle_expanded()
                print (self.text)
                return self.text

    def toggle_expanded(self):
        self.expanded = not self.expanded