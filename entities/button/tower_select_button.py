from entities.button.base_button_class import Button
from constants.global_constants import BLUE, WHITE
import pygame

# TowerSelectButton class inherits from the base Button class
class TowerSelectButton(Button):

    # Class-level list to store all TowerSelectButton instances
    all_tower_select_buttons = []

    def __init__(self, x, y, width, height, text, action, game):
        # Initialize the Button using the parent class constructor
        super().__init__(x, y, width, height, text, action, game)
        self.is_selected = False
        self.selected_color = BLUE
        
        # Add this instance to the class-level list
        self.all_tower_select_buttons.append(self)

    def render(self, screen):
        # Draw button with hover or selected effect
        if self.is_selected:
            pygame.draw.rect(screen, self.selected_color, self.rect)
        elif self.hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        # Draw text centered on button
        text_surface = self.font.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2, 
                                   self.rect.y + (self.rect.height - text_surface.get_height()) // 2))