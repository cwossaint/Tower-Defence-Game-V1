from states.menu_states.base_menu_state_class import MenuState
from constants.gui_constants import MAPSELECTMENUBUTTONDATA

class MapSelectState(MenuState):
    def __init__(self, game, gamestate):
        super().__init__(game)
        self.gamestate = gamestate
        self.state = "mapselect"
        self.title = "Choose Map"
        self.button_data = MAPSELECTMENUBUTTONDATA
        self.create_buttons(game)     

    def update(self):
        output =  super().update()
        if output == "mainmenu":
            return output
        elif output != self.state:
            self.gamestate.grid_manager.load_map_data(output)
            return "playing"
        return self.state
