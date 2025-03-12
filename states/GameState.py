from states.State import *
from entities.Button import *

class GameState(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        # Update game elements, handle player inputs, etc.
        pass

    def render(self):
        # Render the game world and HUD
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
