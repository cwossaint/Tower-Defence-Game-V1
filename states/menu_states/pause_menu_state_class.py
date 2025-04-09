from states.menu_states.base_menu_state_class import MenuState
from constants.gui_constants import PAUSEMENUBUTTONDATA

class PauseState(MenuState):
    def __init__(self, game):
        super().__init__(game)  # Call the base MenuState constructor
        self.state = "pause"  # Identifier for this state; used for transitions or checks
        self.title = "Paused"  # Title that will be displayed on the pause menu screen
        self.button_data = PAUSEMENUBUTTONDATA  # data for buttons to create
        self.create_buttons(game)  # Use base class method to create and position the buttons
