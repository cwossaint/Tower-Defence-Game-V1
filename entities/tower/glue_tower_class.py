from entities.tower.base_tower_class import Tower
from entities.projectile.glue_projectile_class import Glue_Projectile
from entities.sprites import GLUETOWERSPRITE

class Glue(Tower):
    cost = 25  # The cost of placing the Glue tower

    def __init__(self, x, y, range=150, damage=0, attack_delay=70, slow=0.5, splash_range=80, slow_duration=180):
        # Initialize the Glue tower with position, range, damage, and attack delay
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = GLUETOWERSPRITE  # Set the sprite for the Glue tower
        self.find_centre()  # Calculate the center of the tower
        # Initialize additional properties specific to Glue tower
        self.splash_range = splash_range  # Range within which enemies will be affected by the glue
        self.slow = slow  # Percentage by which the enemies are slowed down
        self.slow_duration = slow_duration  # Duration for which the enemies will be slowed
        self.name = 'Glue Tower'  # Name of the tower
        
        # Upgrade stats for different levels of the Glue tower
        self.upgrade_stats = {
            1: { 
                "slow": 0.5,
                "range": 150,
                "attack delay": 70,
                "slow duration": 180,
                "splash range": 80,
                "cost": 25
            },
            2: { 
                "slow": 0.6,
                "range": 175,
                "attack delay": 60,
                "slow duration": 250,
                "splash range": 100,
                "cost": 65
            },
            3: { 
                "slow": 0.8,
                "range": 250,
                "attack delay": 45,
                "slow duration": 300,
                "splash range": 125,
                "cost": 100
            },
        }

    def fire_projectile(self):
        # Fire a projectile if there's a target and enough attack time has passed
        if self.target and self.attack_timer >= self.attack_delay:
            # Set the target coordinates (center of the enemy)
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            # Create a Glue_Projectile and fire it towards the target
            projectile = Glue_Projectile(self.centrex, self.centrey, self.target_coords, self.damage, self.slow, self.splash_range, self.slow_duration)
            self.attack_timer = 0  # Reset the attack timer to prepare for the next shot

    def upgrade(self):
        # Upgrade the Glue tower stats if a higher level is available
        if not self.level + 1 > len(self.upgrade_stats):
            self.level += 1  # Increment the level
            try:
                upgrade_stats = self.upgrade_stats.get(self.level)
                self.slow = upgrade_stats.get("slow")  # Update slow percentage
                self.range = upgrade_stats.get("range")  # Update attack range
                self.attack_delay = upgrade_stats.get("attack delay")  # Update attack delay
                self.slow_duration = upgrade_stats.get("slow duration")  # Update slow duration
                self.splash_range = upgrade_stats.get("splash range")  # Update splash range
            except AttributeError:
                print("error: missing upgrade attribute")
