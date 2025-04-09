from states.menu_states.base_menu_state_class import MenuState
from constants.gui_constants import GAMEOVERMENUDATA

class GameOverState(MenuState):
    def __init__(self, game):
        super().__init__(game)  # Inherit base MenuState attributes
        self.state = "gameover"  # Unique identifier for this state
        self.title = "Game Over"  # Title shown at the top of the screen
        self.button_data = GAMEOVERMENUDATA  # data for buttons to create 
        self.create_buttons(game)  # Generate buttons based on the data
