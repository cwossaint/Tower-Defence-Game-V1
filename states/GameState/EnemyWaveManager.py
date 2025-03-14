from entities.enemy import *


class EnemyWaveManager:

    def create_enemy(self):
        self.path = self.pathfinding_manager.generate_path()
        start_tile = self.pathfinding_manager.locate_start_point()
        row, col = start_tile
        x, y = self.grid_manager.grid_to_screen(row, col)
        enemy = Enemy(x, y, 5, self.path)