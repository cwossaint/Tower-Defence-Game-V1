from entities.button.base_button_class import *
from button_data import *
from constants import *

class GUIManager:
    def __init__(self, game):
        self.buttons = []
        self.selected_tower = None
        self.game = game
        self.wave_start = False
        self.button_data = GAMEGUIPANELBUTTONDATA
        self.create_buttons()
    
    def create_buttons(self):
        num_buttons = len(self.button_data)

        total_button_height = num_buttons * GAMEBUTTONHEIGHT + (num_buttons - 1) * GAMEBUTTONSPACING
        start_y = 0 + (SCREEN_HEIGHT - total_button_height) // 2 
        x_position = (SCREEN_WIDTH - GRID_SIZE  - GAMEBUTTONWIDTH ) // 2 + GRID_SIZE

        for index, (text, output, type) in enumerate(self.button_data):
            y_position = start_y + index * (GAMEBUTTONHEIGHT + GAMEBUTTONSPACING)
            button = type(x_position, y_position, GAMEBUTTONWIDTH, GAMEBUTTONHEIGHT, text, output, self.game)
            self.buttons.append(button)

    def unselect_tower(self):
        self.selected_tower = None
    
    def update(self):
        for button in self.buttons:
            output = button.update()
            if output:
                if isinstance(button, TowerSelectButton):
                    self.selected_tower = output
                elif isinstance(button, WaveStartButton):
                    self.wave_start = True
                elif isinstance(button, MenuButton):
                    return output
                        
            
    def render(self, screen):
        for button in self.buttons:
            button.render(screen)

    def reset(self):
        self.selected_tower = None
        self.wave_start = False