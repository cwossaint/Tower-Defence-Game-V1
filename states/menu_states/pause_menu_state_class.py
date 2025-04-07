from states.menu_states.base_menu_state_class import MenuState
from button_data import PAUSEMENUBUTTONDATA

class PauseState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "pause"
        self.title = "Paused"
        self.button_data = PAUSEMENUBUTTONDATA
        self.create_buttons(game)