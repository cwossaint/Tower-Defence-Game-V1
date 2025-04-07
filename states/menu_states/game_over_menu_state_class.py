from states.menu_states.base_menu_state_class import MenuState
from button_data import GAMEOVERMENUDATA

class GameOverState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "gameover"
        self.title = "Game Over"
        self.button_data = GAMEOVERMENUDATA
        self.create_buttons(game)   