from states.menu_states.base_menu_state_class import MenuState
from button_data import MAINMENUBUTTONDATA

class MainMenuState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "mainmenu"
        self.title = "Main Menu"
        self.button_data = MAINMENUBUTTONDATA
        self.create_buttons(game)
