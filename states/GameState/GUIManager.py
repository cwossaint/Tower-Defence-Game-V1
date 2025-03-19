from entities.Button import *
from states.GameState.GameGUIButtonData import *

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

        total_button_height = num_buttons * BUTTONHEIGHT + (num_buttons - 1) * BUTTONSPACING
        start_y = 0 + (SCREEN_HEIGHT - total_button_height) // 2 
        x_position = (SCREEN_WIDTH - GRID_SIZE  - BUTTONWIDTH ) // 2 + GRID_SIZE

        for index, (text, output, type) in enumerate(self.button_data):
            y_position = start_y + index * (BUTTONHEIGHT + BUTTONSPACING)
            button = type(x_position, y_position, BUTTONWIDTH, BUTTONHEIGHT, text, output, self.game)
            self.buttons.append(button)

    def unselect_tower(self):
        self.selected_tower = None
    
    def update(self):
        for button in self.buttons:
            output = button.handle_event()
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