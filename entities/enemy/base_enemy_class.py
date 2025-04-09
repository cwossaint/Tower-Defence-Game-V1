from constants.global_constants import TILE_SIZE
import pygame

class Enemy():

    # Class-level list to keep track of all enemy instances
    all_enemies = []

    def __init__(self, x, y, directions_list, game_data, wave, health, damage, speed):
        # Position
        self.x = x
        self.y = y

        # Combat stats
        self.health = health
        self.damage = damage
        self.speed = speed

        # Game and wave context
        self.wave = wave
        self.game_data = game_data
        self.directions_list = directions_list
        self.current_direction = None
        self.directions_index = 0
        self.distance_travelled = 0

        # Slow debuff mechanics
        self.slow_debuff = 0
        self.slow_debuff_timer = 0
        self.slow_duration = 0

        # Removal flag
        self.removed = False

        # Add this enemy to the global enemy list
        self.all_enemies.append(self)

    def check_is_dead(self):
        # If health is zero or below, remove the enemy and give player cash
        if self.health <= 0:
            self.remove()
            self.game_data.add_cash(self.value)

    def remove(self):
        # Remove enemy from the game and mark as removed
        if self in Enemy.all_enemies: 
            Enemy.all_enemies.remove(self)
            self.removed = True

    def calculate_distance(self):
        # Calculate the distance to move based on speed and slow effect
        distance_to_travel = self.speed - (self.speed * self.slow_debuff)
        if self.distance_travelled + distance_to_travel > TILE_SIZE:
            distance = TILE_SIZE - self.distance_travelled
        else:
            distance = distance_to_travel
        return distance

    def move(self):
        # Move in the current direction by the calculated distance
        distance = self.calculate_distance()
        if self.current_direction == "left":
            self.x -= distance
        elif self.current_direction == "right":
            self.x += distance
        elif self.current_direction == "up":
            self.y -= distance
        elif self.current_direction == "down":
            self.y += distance

        self.distance_travelled += distance
        self.update_rect()

    def update_rect(self):
        # Update the enemy's collision rect based on its position and sprite
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())

    def update(self):
        # Called every frame to update enemy logic
        self.determine_direction()
        self.move()
        self.check_is_dead()
        self.check_slow()

    def determine_direction(self):
        # Update direction when a full tile has been traveled
        if self.distance_travelled >= TILE_SIZE:
            if not self.end_of_path():
                self.directions_index += 1
                self.distance_travelled = 0
        self.current_direction = self.directions_list[self.directions_index]

    def end_of_path(self):
        # Check if the enemy has reached the end of the path
        if self.directions_index + 1 < len(self.directions_list):
            return False
        else: 
            self.attack_base()
            return True
        
    def get_slowed(self, percentage_slow, slow_duration):
        # Apply a slow debuff if not already slowed
        if self.slow_debuff == 0:
            self.slow_debuff = percentage_slow
            self.slow_duration = slow_duration
            self.slow_debuff_timer = 0

    def check_slow(self):
        # Track and clear slow effect after duration expires
        if self.slow_debuff > 0:
            if self.slow_debuff_timer > self.slow_duration:
                self.slow_debuff = 0
            else: 
                self.slow_debuff_timer += 1
            
    def attack_base(self):
        # Damage the base and remove the enemy
        self.remove()
        self.game_data.remove_lives(self.damage)

    def take_damage(self, damage):
        # Reduce health by damage taken
        self.health -= damage

    def render(self, screen):
        # Draw the enemy on the screen
        screen.blit(self.sprite, (self.x, self.y))

    def scale_stats(self):
        # Scale enemy stats based on the wave number
        self.health *= (1.25 ** self.wave) // 1 
        self.damage *= (1.05 ** self.wave) // 1 
        self.speed *= (1.05 ** self.wave) // 1
