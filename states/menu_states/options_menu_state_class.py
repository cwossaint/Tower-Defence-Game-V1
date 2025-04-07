from states.menu_states.base_menu_state_class import MenuState
from constants.gui_constants import OPTIONSMENUDATA

class OptionsState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "options"
        self.title = "Options"
        self.button_data = OPTIONSMENUDATA
        self.create_buttons(game)     