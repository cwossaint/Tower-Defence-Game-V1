import pygame

class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action  # Action is a function to call when button is pressed
        self.font = pygame.font.SysFont("Arial", 30)
        self.color = (0, 255, 0)  # Default color (green)
        self.hover_color = (255, 255, 0)  # Hover color (yellow)
        self.clicked = False

    def draw(self, screen):
        """Draw the button on the screen."""
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        # Change color if the mouse is hovering over the button
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
            if mouse_click and not self.clicked:
                self.clicked = True
                if self.action:
                    self.action()  # Call the associated action when clicked
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        # Draw the text
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2, 
                                   self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def reset(self):
        """Reset the click state (for next frame)."""
        self.clicked = False
