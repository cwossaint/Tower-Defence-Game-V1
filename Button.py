import pygame

class Button:
    def __init__(self, x, y, width, height, text, output, game):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.output = output  # Action is a function to call when button is pressed
        self.font = pygame.font.SysFont("Arial", 30)
        self.color = (0, 255, 0)  # Default color (green)
        self.hover_color = (255, 255, 0)  # Hover color (yellow)
        self.game = game
        self.hovered = False
        self.pressed = False

    def handle_event(self):
        self.hovered = self.rect.collidepoint(self.game.mouse.x, self.game.mouse.y)
        if self.game.mouse.is_pressed():
            if self.hovered:
                return self.output

    def render(self, screen):

        if self.hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
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

class TowerSelectButton(Button):

    all_tower_select_buttons = []

    def __init__(self, x, y, width, height, text, action, game):
        super().__init__(x, y, width, height, text, action, game)
        self.all_tower_select_buttons.append(self)
    

class MenuButton(Button):

    all_menu_buttons = []

    def __init__(self, x, y, width, height, text, action, game):
        super().__init__(x, y, width, height, text, action, game)
        self.all_menu_buttons.append(self)
    