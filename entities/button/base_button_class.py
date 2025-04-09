from constants.global_constants import WHITE, LAPIS_BLUE, DARK_YELLOW
import pygame
import time

class Button:

    # Cooldown time (in seconds) to prevent rapid multiple presses
    button_cooldown = 0.2
    last_button_press = 0

    def __init__(self, x, y, width, height, text, output, game):
        # Define the button's rectangular area
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text              # Button label
        self.output = output          # Value to return when pressed
        self.font = pygame.font.SysFont("Arial", 30)
        self.color = LAPIS_BLUE       # Default color
        self.hover_color = DARK_YELLOW  # Color when hovered
        self.game = game              # Reference to the game object
        self.hovered = False          # Is mouse over the button?
        self.pressed = False          # Is button currently being pressed?

    def update(self):
        # Get current time for cooldown logic
        current_time = time.time()
        if current_time - Button.last_button_press < Button.button_cooldown:
            pass  # Too soon to register another press
        else:
            # Get current mouse position
            mousex, mousey = pygame.mouse.get_pos()
            self.hovered = self.rect.collidepoint(mousex, mousey)  # Check if mouse is over button
            if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
                if self.hovered:
                    Button.last_button_press = current_time  # Update last press time
                    return self.output  # Return associated output

    def render(self, screen):
        # Draw button with hover effect
        if self.hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        # Draw text centered on button
        text_surface = self.font.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2, 
                                   self.rect.y + (self.rect.height - text_surface.get_height()) // 2))
    
    def is_pressed(self):
        # Check for button press using custom game mouse handler
        if self.rect.collidepoint(self.game.mouse.get_pos) and self.game.mouse.is_pressed:
           return True
        return False
    
    def is_hovering(self):
        # Check if mouse is hovering over the button (not pressed)
        if self.rect.collidepoint(self.game.mouse.get_pos) and not self.game.mouse.is_pressed:
           return True
        return False
