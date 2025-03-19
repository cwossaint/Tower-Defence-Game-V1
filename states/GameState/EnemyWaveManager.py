from entities.enemy import *


class EnemyWaveManager:
    def __init__(self, pathfinding_manager, grid_manager, game_data, guimanager):
        self.pathfinding_manager = pathfinding_manager
        self.grid_manager = grid_manager
        self.game_data = game_data
        self.guimanager = guimanager
        self.path = None
        self.start_point = None
        self.wave = 0
        self.enemies_to_spawn = 0
        self.spawn_timer = 0
        self.spawn_delay = 60
        self.wave_rewards_granted = False

    def find_path(self):
        if self.path == None:
            self.path = self.pathfinding_manager.generate_path() 
            self.start_point = self.pathfinding_manager.locate_start_point()

    def create_enemy(self):
        row, col = self.start_point
        x, y = self.grid_manager.grid_to_screen(row, col)
        enemy = Enemy(x, y, (3 + (100 * 0.2 * self.wave)) // 1, (7 + self.wave // 2), self.path, self.game_data)

    def start_new_wave(self):
        if self.guimanager.wave_start == True:
            self.wave += 1
            self.wave_rewards_granted = False
            self.game_data.next_wave()
            self.enemies_to_spawn = 5 + (2 * self.wave)
            if self.spawn_delay > 10:
                self.spawn_delay = 60 - (5 * self.wave)
            self.guimanager.wave_start = False

    def update(self):
        if self.wave_cleared():
            self.start_new_wave()
        elif self.path:
            if self.spawn_timer >= self.spawn_delay:
                if self.enemies_to_spawn > 0:
                    self.create_enemy()
                    self.spawn_timer = 0 
                    self.enemies_to_spawn -= 1
            else:
                self.spawn_timer += 1
        else:
            self.find_path()
    
    def wave_cleared(self):
        if self.enemies_to_spawn <= 0 and len(Enemy.all_enemies) == 0:
            if self.wave_rewards_granted == False and self.wave > 0:
                self.wave_rewards_granted = True
                self.game_data.add_cash(100 * (0.1 * self.wave))
                self.game_data.set_message("Wave Cleared")
            return True
        return False
    
    def reset(self):
        self.wave = 0
        self.enemies_to_spawn = 0
        self.wave_rewards_granted = False
        self.path = None
        self.start_point = None