from states.menu_states.base_menu_state_class import MenuState
from constants.gui_constants import MAPSELECTMENUBUTTONDATA

class MapSelectState(MenuState):
    def __init__(self, game, gamestate):
        super().__init__(game)  # Initialize the base menu class
        self.gamestate = gamestate  # Reference to the main game state, needed to load map data
        self.state = "mapselect"  # Identifier for this menu state
        self.title = "Choose Map"  # Title text displayed on the screen
        self.button_data = MAPSELECTMENUBUTTONDATA  # data for buttons to create
        self.create_buttons(game)  # Create and position the map selection buttons

    def update(self):
        output = super().update()  # Check if any button was pressed and get the result
        if output == "mainmenu":
            return output  # If "mainmenu" was selected, return to main menu
        elif output != self.state:
            # If a map button was pressed, load that map's data into the game state
            self.gamestate.grid_manager.load_map_data(output)
            return "playing"  # Transition to the actual game (playing) state
        return self.state  # Otherwise, remain in the current state
