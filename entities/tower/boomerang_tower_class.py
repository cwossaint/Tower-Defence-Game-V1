from entities.projectile.boomerang_projectile_class import Boomerang_Projectile
from entities.tower.base_tower_class import Tower
from entities.sprites import BOOMERANGTOWERSPRITE

class Boomerang(Tower):
    cost = 25  # The cost of placing the Boomerang tower
    
    def __init__(self, x, y, range=250, damage=7, attack_delay=50, pierce=5):
        # Initialize the Boomerang tower with position, range, damage, attack delay, and pierce value
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = BOOMERANGTOWERSPRITE  # Set the sprite for the Boomerang tower
        self.find_centre()  # Calculate the center of the tower
        self.pierce = pierce  # Set the pierce value (how many enemies it can hit before disappearing)
        self.name = 'Boomerang Tower'  # Name of the tower
        # Upgrade stats for different levels of the Boomerang tower
        self.upgrade_stats = {
            1: { 
                "damage": 7,
                "range": 250,
                "attack delay": 50,
                "pierce": 5,
                "cost": 25
            },
            2: { 
                "damage": 12,
                "range": 300,
                "attack delay": 45,
                "pierce": 7,
                "cost": 50
            },
            3: { 
                "damage": 20,
                "range": 450,
                "attack delay": 35,
                "pierce": 15,
                "cost": 175
            },
        }
    
    def fire_projectile(self):
        # Fire a projectile if there's a target and enough attack time has passed
        if self.target and self.attack_timer >= self.attack_delay:
            # Set the target coordinates (center of the enemy)
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            # Create a Boomerang_Projectile and fire it towards the target
            projectile = Boomerang_Projectile(self.centrex, self.centrey, self.target_coords, self.damage, self.pierce)
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
                self.pierce = upgrade_stats.get("pierce")  # Update pierce
            except AttributeError:
                # If there is an error in retrieving the upgrade stats, print an error message
                print("error: missing upgrade attribute")
