from constants import WHITE, LAPIS_BLUE, DARK_YELLOW
import pygame
import time

class Button:

    button_cooldown = 0.2
    last_button_press = 0

    def __init__(self, x, y, width, height, text, output, game):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.output = output 
        self.font = pygame.font.SysFont("Arial", 30)
        self.color = LAPIS_BLUE
        self.hover_color = DARK_YELLOW
        self.game = game
        self.hovered = False
        self.pressed = False

    def update(self):
        current_time = time.time()
        if current_time - Button.last_button_press < Button.button_cooldown:
            pass
        else:
            mousex, mousey = pygame.mouse.get_pos()
            self.hovered = self.rect.collidepoint(mousex, mousey)
            if pygame.mouse.get_pressed()[0]:
                if self.hovered:
                    Button.last_button_press = current_time
                    return self.output

    def render(self, screen):

        if self.hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        text_surface = self.font.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2, 
                                   self.rect.y + (self.rect.height - text_surface.get_height()) // 2))
    
    def is_pressed(self):
        if self.rect.collidepoint(self.game.mouse.get_pos) and self.game.mouse.is_pressed:
           return True
        return False
    
    def is_hovering(self):
        if self.rect.collidepoint(self.game.mouse.get_pos) and not self.game.mouse.is_pressed:
           return True
        return False
    
    