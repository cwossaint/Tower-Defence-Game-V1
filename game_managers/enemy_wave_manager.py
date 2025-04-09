from entities.enemy.boss_enemy_class import Boss_Enemy
from entities.enemy.speedy_enemy_class import Speedy_Enemy
from entities.enemy.tanky_enemy_class import Tanky_Enemy
from entities.enemy.basic_enemy_class import Basic_Enemy
from entities.enemy.base_enemy_class import Enemy

class EnemyWaveManager:
    def __init__(self, pathfinding_manager, grid_manager, game_data, guimanager):
        # Managers and game state references
        self.pathfinding_manager = pathfinding_manager
        self.grid_manager = grid_manager
        self.game_data = game_data
        self.guimanager = guimanager

        # Path and wave data
        self.path = None
        self.start_point = None
        self.wave = 0
        self.enemies_to_spawn = 0
        self.spawn_timer = 0
        self.spawn_delay = 60  # Time between spawns (in frames/ticks)
        self.wave_rewards_granted = False

    def find_path(self):
        # Only generate the path once when not already set
        if self.path == None:
            self.path = self.pathfinding_manager.generate_path() 
            self.start_point = self.pathfinding_manager.locate_start_point()

    def create_enemy(self):
        # Spawn an enemy based on pattern rules
        row, col = self.start_point
        x, y = self.grid_manager.grid_to_screen(row, col)

        # Boss every 50th, Speedy every 10th, Tanky every 3rd, Basic otherwise
        if self.enemies_to_spawn % 50 == 0:
            enemy = Boss_Enemy(x, y, self.path, self.game_data, self.wave)
        elif self.enemies_to_spawn % 10 == 0:
            enemy = Speedy_Enemy(x, y, self.path, self.game_data, self.wave)
        elif self.enemies_to_spawn % 3 == 0:
            enemy = Tanky_Enemy(x, y, self.path, self.game_data, self.wave)
        elif self.enemies_to_spawn % 1 == 0:
            enemy = Basic_Enemy(x, y, self.path, self.game_data, self.wave)

    def start_new_wave(self):
        # Triggered by the GUI start button
        if self.guimanager.wave_start == True:
            self.wave += 1
            self.wave_rewards_granted = False
            self.game_data.next_wave()

            # Calculate number of enemies for the wave
            self.enemies_to_spawn = 10 + (7 * self.wave)

            # Reduce spawn delay for faster waves, with a minimum cap
            if self.spawn_delay > 3:
                self.spawn_delay = 60 - (5 * self.wave)

            # Reset GUI wave start trigger
            self.guimanager.wave_start = False

    def update(self):
        # Core update loop to handle wave logic
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
        # Check if wave is finished and grant rewards
        if self.enemies_to_spawn <= 0 and len(Enemy.all_enemies) == 0:
            if self.wave_rewards_granted == False and self.wave > 0:
                self.wave_rewards_granted = True
                self.game_data.add_cash(100 * (0.1 * self.wave))
                self.game_data.set_message("Wave Cleared")
            return True
        return False

    def reset(self):
        # Reset wave manager for a new game
        self.wave = 0
        self.enemies_to_spawn = 0
        self.spawn_delay = 60
        self.wave_rewards_granted = False
        self.path = None
        self.start_point = None
