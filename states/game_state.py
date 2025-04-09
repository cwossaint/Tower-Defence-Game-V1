from states.base_state_class import State
from game_managers.map_manager import MapManager
from constants.global_constants import *
from entities.tower.base_tower_class import Tower
from game_managers.grid_manager import GridManager
from game_managers.game_gui_manager import GUIManager
from game_managers.pathfinding_manager import PathfindingManager
from entities.enemy.base_enemy_class import Enemy
from game_managers.enemy_wave_manager import EnemyWaveManager
from game_managers.game_data_manager import GameDataManager
from game_managers.tower_edit_manager import TowerEditGUIManager
from entities.projectile.basic_projectile_class import Projectile
import pygame


class GameState(State):
    def __init__(self, game):
        super().__init__(game)

        # Manages the player's in-game data such as health, cash, messages, etc.
        self.game_data = GameDataManager()

        # Manages the side-panel GUI where towers can be selected, waves started, etc.
        self.guimanager = GUIManager(game)

        # Manages the tile grid, tower placement, and tile values (like obstacles or paths)
        self.grid_manager = GridManager(game, self.guimanager, self.game_data)

        # Manages the GUI shown when a tower is selected for editing (upgrading/removing)
        self.tower_edit_guimanager = TowerEditGUIManager(game, self.grid_manager, self.game_data)

        # Handles pathfinding logic and generates the path enemies follow
        self.pathfinding_manager = PathfindingManager(self.grid_manager)

        # Manages enemy wave spawning and wave progression
        self.enemy_wave_manager = EnemyWaveManager(
            self.pathfinding_manager,
            self.grid_manager,
            self.game_data,
            self.guimanager
        )

        # Responsible for rendering the map grid and obstacles on the screen
        self.game_map = MapManager(game, self.grid_manager)

        # Represents the current game state (used to control transitions like pause/gameover)
        self.state = "playing"


    def render(self, screen):
        self.game_map.draw_map_obstacles(screen)
        self.game_map.render(screen)

        # GUI rendered depends on whether a tower is selected
        if not self.grid_manager.selected_placed_tower:
            self.guimanager.render(screen)
        else:
            self.tower_edit_guimanager.render(screen)

        x, y = pygame.mouse.get_pos()

        # Draw all entities
        for tower in Tower.all_towers:
            tower.render(screen)

        for enemy in Enemy.all_enemies:
            enemy.render(screen)

        for projectile in Projectile.all_projectiles:
            projectile.render(screen)

        # Tile highlight to show hovered tile
        if x + 1 < GRID_SIZE:
            self.game_map.highlight_tile(screen)

        self.game_data.render(screen)


    def reset(self):

        #reset all data to original values, clear all entity objects
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

        x, y = pygame.mouse.get_pos()

        # GUI button interaction (right panel)
        if (x + 1) > GRID_SIZE:
            if not self.grid_manager.selected_placed_tower:
                state = self.guimanager.update()
                if state:
                    return state

        # Tower placement or selection (grid area)
        if (x + 1) < GRID_SIZE:
            self.grid_manager.update()

        # Tower edit GUI
        if self.grid_manager.selected_placed_tower:
            self.tower_edit_guimanager.update()

        self.game_data.update()

        # Update all active entities
        for enemy in Enemy.all_enemies:
            enemy.update()
        for tower in Tower.all_towers:
            tower.update()
        for projectile in Projectile.all_projectiles:
            projectile.update()

        # Check if player has lost
        if self.game_data.game_over():
            return "gameover"

        return "playing"

    
