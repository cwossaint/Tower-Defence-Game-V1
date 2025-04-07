from states.base_state_class import *
from entities.button.base_button_class import *
from constants import *
from button_data import *


class MenuState(State):
    def __init__(self, game, x=0, y=0):
        super().__init__(game)
        self.buttons = []
        self.background = None
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("Arial", 100)

    def create_buttons(self, game):

        num_buttons = len(self.button_data)

        total_button_height = num_buttons * MENUBUTTONHEIGHT + (num_buttons - 1) * MENUBUTTONSPACING
        start_y = self.y + (SCREEN_HEIGHT - total_button_height) // 2 + MENUTEXTSPACE
        x_position = (SCREEN_WIDTH  - MENUBUTTONWIDTH )// 2

        for index, (text, output) in enumerate(self.button_data):
            y_position = start_y + index * (MENUBUTTONHEIGHT + MENUBUTTONSPACING)
            button = MenuButton(x_position, y_position, MENUBUTTONWIDTH, MENUBUTTONHEIGHT, text, output, game)
            self.buttons.append(button)

    def update(self):
        for button in self.buttons:
            output = button.update()
            if output:
                return output
        return self.state


    def center_text(self, screen, text):

        text_rect = text.get_rect()
        text_rect.centerx = SCREEN_WIDTH // 2  
        text_rect.y = 50  
        screen.blit(text, text_rect)

    def render(self, screen):

        title = self.font.render((self.title), True, WHITE)
        self.center_text(screen, title)

       # screen.blit(self.background, self.x, self.
        for button in self.buttons:
            button.render(screen)


