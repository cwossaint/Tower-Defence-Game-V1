from states.menu_states.base_menu_state_class import MenuState
from constants.gui_constants import OPTIONSMENUDATA

class OptionsState(MenuState):
    def __init__(self, game):
        super().__init__(game)  # Initialize the base menu class (MenuState)
        self.state = "options"  # Identifier for this specific menu state
        self.title = "Options :D "  # Title text shown at the top of the options menu
        self.button_data = OPTIONSMENUDATA  # data for buttons to create
        self.create_buttons(game)  # Generate and position the buttons based on the data
