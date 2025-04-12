from entities.projectile.cannon_projectile_class import Cannon_Projectile
from entities.tower.base_tower_class import Tower
from entities.sprites import CANNONTOWERSPRITE

class Cannon(Tower):
    cost = 70  # The cost of placing the Cannon tower
    
    def __init__(self, x, y, range=175, damage=80, attack_delay=100, splash_damage=35, splash_range=125):
        # Initialize the Cannon tower with position, range, damage, attack delay, splash damage, and splash range
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = CANNONTOWERSPRITE  # Set the sprite for the Cannon tower
        self.find_centre()  # Calculate the center of the tower
        self.splash_damage = splash_damage  # Set the splash damage value
        self.splash_range = splash_range  # Set the splash range (area of effect)
        self.name = 'Cannon Tower'  # Name of the tower
        # Upgrade stats for different levels of the Cannon tower
        self.upgrade_stats = {
            1: { 
                "damage": 80,
                "range": 175,
                "attack delay": 100,
                "cost": 70,
                "splash damage": 35,
                "splash range": 125
            },
            2: { 
                "damage": 95,
                "range": 200,
                "attack delay": 95,
                "cost": 75,
                "splash damage": 45,
                "splash range": 150
            },
            3: { 
                "damage": 120,
                "range": 225,
                "attack delay": 85,
                "cost": 125,
                "splash damage": 65,
                "splash range": 200
            },
        }
    
    def fire_projectile(self):
        # Fire a projectile if there's a target and enough attack time has passed
        if self.target and self.attack_timer >= self.attack_delay:
            # Set the target coordinates (center of the enemy)
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            # Create a Cannon_Projectile and fire it towards the target with splash damage and splash range
            projectile = Cannon_Projectile(self.centrex, self.centrey, self.target_coords, self.damage, self.splash_damage, self.splash_range)
            self.attack_timer = 0  # Reset the attack timer

    def upgrade(self):
        # Upgrade the tower to the next level if possible
        if not self.level + 1 > len(self.upgrade_stats):
            self.level += 1  # Increase the level of the tower
            try:
                # Get the upgrade stats for the new level
                upgrade_stats = self.upgrade_stats.get(self.level)
                self.damage = upgrade_stats.get("damage")  # Update damage
                self.range = upgrade_stats.get("range")  # Update range
                self.attack_delay = upgrade_stats.get("attack delay")  # Update attack delay
                self.splash_range = upgrade_stats.get("splash range")  # Update splash range
                self.splash_damage = upgrade_stats.get("splash damage")  # Update splash damage
            except AttributeError:
                # If there is an error in retrieving the upgrade stats, print an error message
                print("error: missing upgrade attribute")
