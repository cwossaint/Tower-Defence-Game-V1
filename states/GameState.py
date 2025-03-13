from states.State import *
from entities.Button import *
from GridManager import *
from GUIManager import *

class GameState(State):
    def __init__(self, game):
        super().__init__(game)
        self.grid_manager = GridManager(game)
        self.guimanager = GUIManager()

    def update(self):
        # Update game elements, handle player inputs, etc.
        pass

    def render(self):

        pass


class PlayingState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "playing"
        self.buttons = []

    def create_buttons():
        pass
    
    def update(self):
        # Update the game loop, move enemies, attack with towers, etc.
        pass

    def render(self):
        # Draw the game objects, enemies, and towers
        pass
