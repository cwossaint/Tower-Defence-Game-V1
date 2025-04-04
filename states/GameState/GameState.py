from states.State import *
from states.GameState.map import *
from constants import *
from entities.tower import *
from states.GameState.GridManager import *
from states.GameState.GUIManager import *
from states.GameState.PathfinderManager import *
from entities.enemy import *
from states.GameState.EnemyWaveManager import *
from states.GameState.GameData import *
from states.GameState.TowerEditGUIManager import *


class GameState(State):
    def __init__(self, game):
        super().__init__(game)
        self.game_data = GameData()
        self.guimanager = GUIManager(game)
        self.grid_manager = GridManager(game, self.guimanager, self.game_data)
        self.tower_edit_guimanager = TowerEditGUIManager(game, self.grid_manager, self.game_data)
        self.pathfinding_manager = PathfindingManager(self.grid_manager)
        self.enemy_wave_manager = EnemyWaveManager(self.pathfinding_manager, self.grid_manager, self.game_data, self.guimanager)
        self.game_map = Map(game, self.grid_manager)
        self.state = "playing"

    def render(self, screen):
        self.game_map.draw_map_obstacles(screen)
        self.game_map.render(screen)
        if not self.grid_manager.selected_placed_tower:
            self.guimanager.render(screen)
        elif self.grid_manager.selected_placed_tower:
            self.tower_edit_guimanager.render(screen)

        x, y = self.game.mouse.get_position()

        for tower in Tower.all_towers:
            tower.render(screen)

        for enemy in Enemy.all_enemies:
            enemy.render(screen)

        for projectile in Projectile.all_projectiles:
            projectile.render(screen)

        if x + 1 < GRID_SIZE:
            self.game_map.highlight_tile(screen)

        self.game_data.render(screen)

    def reset(self):
        self.guimanager.reset()
        self.grid_manager.reset()
        self.game_data.reset()
        self.enemy_wave_manager.reset()
        self.pathfinding_manager.reset()
        Tower.all_towers = []
        Projectile.all_projectiles = []
        Enemy.all_enemies = []

    def update(self):

        if self.grid_manager.array != None:
            self.enemy_wave_manager.update()

        x, y = self.game.mouse.get_position()
        if (x + 1) > GRID_SIZE:
            if not self.grid_manager.selected_placed_tower:
                state = self.guimanager.update()
                if state:
                    return state

        if (x + 1) < GRID_SIZE:
            self.grid_manager.update()

        if self.grid_manager.selected_placed_tower:
                self.tower_edit_guimanager.update()

        self.game_data.update()

        for enemy in Enemy.all_enemies:
            enemy.update()
        for tower in Tower.all_towers:
            tower.update()
        for projectile in Projectile.all_projectiles:
            projectile.update()

        if self.game_data.game_over():
            return "gameover"
            
        return "playing"
    
