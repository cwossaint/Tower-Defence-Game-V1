from entities.tower.base_tower_class import *
from constants.gui_constants import *
from constants.global_constants import *


class TowerEditGUIManager():
    def __init__(self, game, grid_manager, game_date):
        self.game = game
        self.grid_manager = grid_manager
        self.game_data = game_date
        self.tower_stats_text = []
        self.upgrade_stats_text = []
        self.text_spacing = 30
        self.button_data = TOWEREDITGUIBUTTONDATA
        self.font = pygame.font.SysFont("Arial", 25)
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        num_buttons = len(self.button_data)

        total_button_height = num_buttons * GAMEBUTTONHEIGHT + (num_buttons - 1) * GAMEBUTTONSPACING
        start_y = 0 + (SCREEN_HEIGHT - total_button_height) // 2 
        x_position = (SCREEN_WIDTH - GRID_SIZE  - GAMEBUTTONWIDTH ) // 2 + GRID_SIZE

        for index, (text, output, type) in enumerate(self.button_data):
            y_position = start_y + index * (GAMEBUTTONHEIGHT + GAMEBUTTONSPACING)
            button = type(x_position, y_position, GAMEBUTTONWIDTH, GAMEBUTTONHEIGHT, text, output, self.game)
            self.buttons.append(button)

    def render(self, screen):
        for button in self.buttons:
            button.render(screen)
        current_y = 0 - self.text_spacing
        for item in self.tower_stats_text:
            current_y += self.text_spacing
            text = self.font.render((item), True, WHITE)
            screen.blit(text, (780, current_y))
        current_y = 500
        for item in self.upgrade_stats_text:
            current_y += self.text_spacing
            text = self.font.render((item), True, WHITE)
            screen.blit(text, (780, current_y))

    def update(self):
            
            if self.grid_manager.selected_placed_tower:
                tower = self.grid_manager.selected_placed_tower

                current_upgrade_stats = tower.upgrade_stats[tower.level]

                self.upgrade_stats_text = []
                self.tower_stats_text = []

                self.tower_stats_text.append(str(tower.name))
                for stat in current_upgrade_stats:
                    self.tower_stats_text.append(str(stat) + ": " + str(current_upgrade_stats[stat]))

                if not tower.level + 1 > len(tower.upgrade_stats):

                    next_upgrade_stats = tower.upgrade_stats[tower.level + 1]

                    self.upgrade_stats_text.append("level: " + str(tower.level) + "->" + str(tower.level+1))

                    for stat in next_upgrade_stats:
                        if stat != "cost":
                            self.upgrade_stats_text.append(str(stat) + ": " + str(current_upgrade_stats[stat]) + "->" + str(next_upgrade_stats[stat]))
                    upgrade_cost = current_upgrade_stats["cost"]
                    self.upgrade_stats_text.append("cost: " + str(upgrade_cost))

                else: 
                    self.upgrade_stats_text.append("Max Level")

            for button in self.buttons:
                output = button.update()
                if output:
                    tower = self.grid_manager.selected_placed_tower
                    if output == "back":
                        self.grid_manager.selected_placed_tower = None
                    elif output == "remove":
                       tower.remove_tower()
                       x, y = tower.x, tower.y
                       row, col = self.grid_manager.screen_to_grid(x, y)
                       self.grid_manager.set_tile_value(row, col, 0)
                    elif output == "upgrade": 
                        if not tower.level + 1 > len(tower.upgrade_stats):
                            if self.game_data.cash >= upgrade_cost:
                                self.game_data.remove_cash(upgrade_cost)
                                tower.upgrade()
                            else: 
                                self.game_data.set_message("not enough money")


    def monkey(self, tower):
                self.tower_stats_text.append(str(tower.name))
                self.tower_stats_text.append("Level: " + str(tower.level))
                self.tower_stats_text.append("Damage: " + str(tower.damage))
                self.tower_stats_text.append("Attack Delay: " + str(tower.attack_delay))
                self.tower_stats_text.append("Range: " + str(tower.range))

                upgrade_stats = tower.upgrade_stats.get(tower.level + 1)

                if upgrade_attack_delay:

                    upgrade_damage = upgrade_stats.get("damage")
                    upgrade_range = upgrade_stats.get("range")
                    upgrade_attack_delay = upgrade_stats.get("attack delay")
                    upgrade_cost = upgrade_stats.get("cost")

                    self.upgrade_stats_text.append("Upgrade Cost: " + str(upgrade_cost))
                    self.upgrade_stats_text.append("Level: " + str(tower.level) + "->" + str(tower.level + 1))
                    self.upgrade_stats_text.append("Damage: " + str(tower.damage) + "->" + str(upgrade_damage))
                    self.upgrade_stats_text.append("Attack Delay: " + str(tower.attack_delay) + "->" + str(upgrade_attack_delay))
                    self.upgrade_stats_text.append("Range: " + str(tower.range)  + "->" + str(upgrade_range))