from entities.projectile.basic_projectile_class import Basic_Projectile
from entities.tower.base_tower_class import Tower
from entities.sprites import GATLINGTOWERSPRITE

class Gatling(Tower):
    cost = 110  # The cost of placing the Gatling tower
    
    def __init__(self, x, y, range=250, damage=2, attack_delay=5):
        # Initialize the Gatling tower with position, range, damage, and attack delay
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = GATLINGTOWERSPRITE  # Set the sprite for the Gatling tower
        self.find_centre()  # Calculate the center of the tower
        self.projectile_type = "Gatling"  # Set the type of projectile to "Gatling"
        self.name = 'Gatling Tower'  # Name of the tower
        # Upgrade stats for different levels of the Gatling tower
        self.upgrade_stats = {
            1: { 
                "damage": 3,
                "range": 250,
                "attack delay": 5,
                "cost": 110
            },
            2: { 
                "damage": 3.5,
                "range": 325,
                "attack delay": 4.5,
                "cost": 80
            },
            3: { 
                "damage": 6,
                "range": 375,
                "attack delay": 3.75,
                "cost": 120
            },
        }

    def fire_projectile(self):
        # Fire a projectile if there's a target and enough attack time has passed
        if self.target and self.attack_timer >= self.attack_delay:
            # Set the target coordinates (center of the enemy)
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            # Create a Basic_Projectile and fire it towards the target
            projectile = Basic_Projectile(self.centrex, self.centrey, self.target_coords, self.damage)
            self.attack_timer = 0  # Reset the attack timer to prepare for the next shot
