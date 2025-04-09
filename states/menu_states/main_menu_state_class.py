from states.menu_states.base_menu_state_class import MenuState
from constants.gui_constants import MAINMENUBUTTONDATA

class MainMenuState(MenuState):
    def __init__(self, game):
        super().__init__(game)  # Initialize the base MenuState with the game instance
        self.state = "mainmenu"  # Identifier for the main menu state
        self.title = "Main Menu"  # Title text displayed at the top of the screen
        self.button_data = MAINMENUBUTTONDATA  # data for buttons to create
        self.create_buttons(game)  # Create and position the buttons on the screen
