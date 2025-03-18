from entities.enemy import *


class EnemyWaveManager:
    def __init__(self, pathfinding_manager, grid_manager, game_data):
        self.pathfinding_manager = pathfinding_manager
        self.grid_manager = grid_manager
        self.game_data = game_data
        self.path = None
        self.start_point = None
        self.wave = 0
        self.enemies_to_spawn = 5
        self.spawn_timer = 0
        self.spawn_delay = 60

    def find_path(self):
        if self.path == None:
            self.path = self.pathfinding_manager.generate_path() 
            self.start_point = self.pathfinding_manager.locate_start_point()

    def create_enemy(self):
        row, col = self.start_point
        x, y = self.grid_manager.grid_to_screen(row, col)
        enemy = Enemy(x, y, 30 * (0.2 * self.wave), 5, self.path, self.game_data)

    def start_new_wave(self):
        self.wave += 1
        self.game_data.next_wave()
        self.game_data.add_cash(100 * (0.1 * self.wave))
        self.enemies_to_spawn = 5 + (2 * self.wave)
        if self.spawn_delay > 10:
            self.spawn_delay = 60 - (5 * self.wave)
        print("next wave")

    def update(self):
        if self.path:
            if self.spawn_timer >= self.spawn_delay:
                self.create_enemy()
                self.spawn_timer = 0 
                self.enemies_to_spawn -= 1
            else:
                self.spawn_timer += 1
            if self.enemies_to_spawn == 0:
                self.start_new_wave()
        else:
            self.find_path()