from states.base_state_class import *
from entities.button.base_button_class import *
from constants.global_constants import *
from constants.gui_constants import *

class MenuState(State):
    def __init__(self, game, x=0, y=0):
        super().__init__(game)
        self.buttons = []  # Holds menu buttons
        self.background = None  # Optional background image (not yet implemented)
        self.x = x  # Optional offset x for background
        self.y = y  # Optional offset y for background
        self.font = pygame.font.SysFont("Arial", 100)  # Title font

    def create_buttons(self, game):
        num_buttons = len(self.button_data)  # Get number of buttons to create

        # Calculate the total height of all buttons with spacing
        total_button_height = num_buttons * MENUBUTTONHEIGHT + (num_buttons - 1) * MENUBUTTONSPACING
        # Start Y to vertically center buttons (with extra space for title text)
        start_y = self.y + (SCREEN_HEIGHT - total_button_height) // 2 + MENUTEXTSPACE
        # X position to center buttons horizontally
        x_position = (SCREEN_WIDTH - MENUBUTTONWIDTH) // 2

        # Create each button from button_data (text, output)
        for index, (text, output) in enumerate(self.button_data):
            y_position = start_y + index * (MENUBUTTONHEIGHT + MENUBUTTONSPACING)
            button = MenuButton(x_position, y_position, MENUBUTTONWIDTH, MENUBUTTONHEIGHT, text, output, game)
            self.buttons.append(button)

    def update(self):
        # Check each button for user interaction
        for button in self.buttons:
            output = button.update()
            if output:  # If a button was clicked, return its output (usually a state change)
                return output
        return self.state  # Default: stay in current state

    def center_text(self, screen, text):
        # Utility method to center text at the top of the screen
        text_rect = text.get_rect()
        text_rect.centerx = SCREEN_WIDTH // 2  
        text_rect.y = 50  # Distance from the top
        screen.blit(text, text_rect)

    def render(self, screen):
        # Render the menu title
        title = self.font.render((self.title), True, WHITE)
        self.center_text(screen, title)

        # Render all buttons
        for button in self.buttons:
            button.render(screen)
