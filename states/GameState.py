from states.State import *
from map import *
from constants import *
from GridManager import *
from GUIManager import *

class GameState(State):
    def __init__(self, game):
        super().__init__(game)
        self.guimanager = GUIManager(game)
        self.grid_manager = GridManager(game, self.guimanager)
        self.game_map = Map(game, self.grid_manager)
        self.state = "playing"

    def update(self):
        # Update game elements, handle player inputs, etc.
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.guimanager.render(screen)
        self.game_map.render(screen)
        self.game_map.highlight_tile(screen)
        pass

    def handle_event(self):
        x, y = self.game.mouse.get_position()
        if x + 1 > GRID_SIZE:
            self.guimanager.update()
        if x + 1 < GRID_SIZE:
            self.grid_manager.handle_event()
        return "playing"