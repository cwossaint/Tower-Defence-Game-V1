from states.State import *
from map import *
from constants import *
from GridManager import *
from GUIManager import *
from PathfinderManager import *
from entities.enemy import *

class GameState(State):
    def __init__(self, game):
        super().__init__(game)
        self.guimanager = GUIManager(game)
        self.grid_manager = GridManager(game, self.guimanager)
        self.game_map = Map(game, self.grid_manager)
        self.pathfinding_manager = PathfindingManager(self.grid_manager)
        self.path = None
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
        for enemy in Enemy.all_enemies:
            enemy.render(screen)
        if x + 1 < GRID_SIZE:
            self.game_map.highlight_tile(screen)
    

    def handle_event(self):
        if self.path:
            x, y = self.game.mouse.get_position()
            if (x + 1) > GRID_SIZE:
                self.guimanager.update()
            if (x + 1) < GRID_SIZE:
                self.grid_manager.handle_event()
            for enemy in Enemy.all_enemies:
              enemy.update()
        else:
            self.path = self.pathfinding_manager.generate_path()
            start_tile = self.pathfinding_manager.locate_start_point()
            row, col = start_tile
            x, y = self.grid_manager.grid_to_screen(row, col)
            enemy = Enemy(x, y, 5, self.path)
        return "playing"
        