from states.State import *
from map import *
from constants import *
from GridManager import *
from GUIManager import *
from PathfinderManager import *

class GameState(State):
    def __init__(self, game):
        super().__init__(game)
        self.guimanager = GUIManager(game)
        self.grid_manager = GridManager(game, self.guimanager)
        self.game_map = Map(game, self.grid_manager)
        self.pathfinding_manager = PathfindingManager(self.grid_manager)
        self.state = "playing"

    def update(self):
        pass

    def render(self, screen):
        self.game_map.draw_map_obstacles(screen)
        self.guimanager.render(screen)
        self.game_map.render(screen)
        x, y = self.game.mouse.get_position()
        for tower in Tower.all_towers:
            tower.render(screen)
        if x + 1 < GRID_SIZE:
            self.game_map.highlight_tile(screen)
    

    def handle_event(self):
        x, y = self.game.mouse.get_position()
        if (x + 1) > GRID_SIZE:
            self.guimanager.update()
        if (x + 1) < GRID_SIZE:
            self.grid_manager.handle_event()
        return "playing"