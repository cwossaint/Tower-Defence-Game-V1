from entities.projectile.basic_projectile_class import Basic_Projectile
from entities.tower.base_tower_class import Tower
from entities.sprites import DARTTOWERSPRITE


class Dart(Tower):
    cost = 25  # The cost of placing the Dart tower
    
    def __init__(self, x, y, range=150, damage=15, attack_delay=25):
        # Initialize the Dart tower with position, range, damage, and attack delay
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = DARTTOWERSPRITE  # Set the sprite for the Dart tower
        self.find_centre()  # Calculate the center of the tower
        self.projectile_type = "Dart"  # Set the type of projectile to "Dart"
        self.name = 'Dart Tower'  # Name of the tower
        # Upgrade stats for different levels of the Dart tower
        self.upgrade_stats = {
            1: { 
                "damage": 15,
                "range": 150,
                "attack delay": 25,
                "cost": 25
            },
            2: { 
                "damage": 18,
                "range": 175,
                "attack delay": 23,
                "cost": 35
            },
            3: { 
                "damage": 25,
                "range": 250,
                "attack delay": 20,
                "cost": 55
            },
            4: { 
                "damage": 25,
                "range": 500,
                "attack delay": 1,
                "cost": 1000
            },
        }

    def fire_projectile(self):
        # Fire a projectile if there's a target and enough attack time has passed
        if self.target and self.attack_timer >= self.attack_delay:
            # Set the target coordinates (center of the enemy)
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            # Create a Basic_Projectile and fire it towards the target
            projectile = Basic_Projectile(self.centrex, self.centrey, self.target_coords, self.damage)
            self.attack_timer = 0  # Reset the attack timer
