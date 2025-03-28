from entities.tower import *
from states.GameState.GameGUIButtonData import *


class TowerEditGUIManager():
    def __init__(self, game, grid_manager):
        self.game = game
        self.grid_manager = grid_manager
        self.text = ""
        self.button_data = TOWEREDITGUIBUTTONDATA
        self.buttons = []
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

    def render(self, screen):
        for button in self.buttons:
            button.render(screen)

    def update(self):
            if self.grid_manager.selected_placed_tower:
                self.text = ""

            for button in self.buttons:
                output = button.handle_event()
                if output:
                    if output == "remove":
                       self.grid_manager.selected_placed_tower.remove_tower()
                       x, y = self.grid_manager.selected_placed_tower.x, self.grid_manager.selected_placed_tower.y
                       row, col = self.grid_manager.screen_to_grid(x, y)
                       self.grid_manager.set_tile_value(row, col, 0)
                    elif output == "upgrade":
                        print("upgrade" + str(self.grid_manager.selected_placed_tower))

