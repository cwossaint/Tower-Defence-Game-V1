from entities.enemy.base_enemy_class import *
import math

# Base class for all tower types
class Tower():

    all_towers = []  # Class-level list to track all tower instances

    def __init__(self, x, y, range=100, damage=1, attack_delay=10):
        # Initialize tower position and combat stats
        self.sprite = None  # Will hold the tower image
        self.projectile_type = None  # Type of projectile it fires
        self.range = range  # Attack range
        self.damage = damage  # Damage per hit
        self.attack_delay = attack_delay  # Frames between attacks
        self.attack_timer = 0  # Timer to track when the tower can attack again
        self.x = x  # Top-left x coordinate of tower
        self.y = y  # Top-left y coordinate of tower
        self.centrex = 0  # Centre x (for distance calc)
        self.centrey = 0  # Centre y (for distance calc)
        self.target_coords = None  # Coordinates of current target (not used here)
        self.target = None  # Enemy object currently being targeted
        self.level = 1  # Upgrade level
        self.upgrade_stats = {}  # Dict holding upgrade values per level
        self.all_towers.append(self)  # Add this instance to the class list

    def find_centre(self):
        # Calculate the centre point of the tower for targeting
        self.centrex = self.x + (self.sprite.get_width() / 2)
        self.centrey = self.y + (self.sprite.get_height()  / 2)

    def find_target(self):
        # Determine the closest enemy within range to target
        closest_enemy = None
        min_distance = self.range  

        for enemy in Enemy.all_enemies:  # Loop through all active enemies
            distance = self.find_distance(enemy)
            if distance < self.range and distance < min_distance:
                closest_enemy = enemy
                min_distance = distance  

        if closest_enemy:
            self.target = closest_enemy  # Set the closest enemy as target
        else:
            self.target = None  # No valid target found

    def find_distance(self, enemy):
        # Calculate Euclidean distance between tower centre and enemy
        distance = math.sqrt((enemy.x - self.centrex) ** 2 + (enemy.y - self.centrey) ** 2)
        return distance

    def remove_tower(self):
        # Remove this tower instance from the list of all towers
        if self in Tower.all_towers:
            Tower.all_towers.remove(self)

    def fire_projectile(self):
        # Placeholder to be implemented by subclasses (specific tower types)
        pass

    def update(self):
        # Update logic called each frame

        # If no target or target is out of range or removed, find a new one
        if not self.target or self.find_distance(self.target) > self.range or self.target.removed == True:
            self.find_target()

        # If a valid target exists, fire a projectile
        if self.target:
            self.fire_projectile()

        # Increase the attack timer for delay tracking
        self.attack_timer += 1

    def render(self, screen):
        # Draw the tower sprite on the screen at its position
        screen.blit(self.sprite, (self.x, self.y))

    def upgrade(self):
        # Upgrade the tower if not at max level
        if not self.level + 1 > len(self.upgrade_stats):
            self.level += 1  # Increment level
            try:
                upgrade_stats = self.upgrade_stats.get(self.level)  # Get stat changes for new level
                self.damage = upgrade_stats.get("damage")  # Apply new damage value
                self.range = upgrade_stats.get("range")  # Apply new range
                self.attack_delay = upgrade_stats.get("attack delay")  # Apply new attack delay
            except AttributeError:
                print("error: missing upgrade attribute")