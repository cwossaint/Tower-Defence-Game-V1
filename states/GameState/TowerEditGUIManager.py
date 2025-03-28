from entities.tower import *
from states.GameState.GameGUIButtonData import *


class TowerEditGUIManager():
    def __init__(self, game, grid_manager):
        self.game = game
        self.grid_manager = grid_manager
        self.tower_stats_text = []
        self.upgrade_stats_text = []
        self.text_spacing = 40
        self.button_data = TOWEREDITGUIBUTTONDATA
        self.font = pygame.font.SysFont("Arial", 30)
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        num_buttons = len(self.button_data)

        total_button_height = num_buttons * BUTTONHEIGHT + (num_buttons - 1) * BUTTONSPACING
        start_y = 0 + (SCREEN_HEIGHT - total_button_height) // 2 
        x_position = (SCREEN_WIDTH - GRID_SIZE  - BUTTONWIDTH ) // 2 + GRID_SIZE

        for index, (text, output, type) in enumerate(self.button_data):
            y_position = start_y + index * (BUTTONHEIGHT + BUTTONSPACING)
            button = type(x_position, y_position, BUTTONWIDTH, BUTTONHEIGHT, text, output, self.game)
            self.buttons.append(button)

    def render(self, screen):
        for button in self.buttons:
            button.render(screen)
        current_y = 0
        for item in self.tower_stats_text:
            current_y += self.text_spacing
            text = self.font.render((item), True, WHITE)
            screen.blit(text, (780, current_y))
        current_y = 475
        for item in self.upgrade_stats_text:
            current_y += self.text_spacing
            text = self.font.render((item), True, WHITE)
            screen.blit(text, (780, current_y))

    def update(self):
            
            if self.grid_manager.selected_placed_tower:
                tower = self.grid_manager.selected_placed_tower
                self.upgrade_stats_text = []
                self.tower_stats_text = []
                self.tower_stats_text.append(str(tower.name))
                self.tower_stats_text.append("Level: " + str(tower.level))
                self.tower_stats_text.append("Damage: " + str(tower.damage))
                self.tower_stats_text.append("Attack Delay: " + str(tower.attack_delay))
                self.tower_stats_text.append("Range: " + str(tower.range))


                if not tower.level + 1 > len(tower.upgrade_stats):
                    upgrade_stats = tower.upgrade_stats.get(tower.level + 1)
                    upgrade_damage = upgrade_stats.get("damage")
                    upgrade_range = upgrade_stats.get("range")
                    upgrade_attack_delay = upgrade_stats.get("attack delay")

                    self.upgrade_stats_text.append("Upgrade Cost: " + str(0))
                    self.upgrade_stats_text.append("Level: " + str(tower.level) + "->" + str(tower.level + 1))
                    self.upgrade_stats_text.append("Damage: " + str(tower.damage) + "->" + str(upgrade_damage))
                    self.upgrade_stats_text.append("Attack Delay: " + str(tower.attack_delay) + "->" + str(upgrade_attack_delay))
                    self.upgrade_stats_text.append("Range: " + str(tower.range)  + "->" + str(upgrade_range))
                else: 
                    self.upgrade_stats_text.append("Max Level")

            for button in self.buttons:
                output = button.handle_event()
                if output:
                    tower = self.grid_manager.selected_placed_tower
                    if output == "remove":
                       tower.remove_tower()
                       x, y = tower.x, tower.y
                       row, col = self.grid_manager.screen_to_grid(x, y)
                       self.grid_manager.set_tile_value(row, col, 0)
                    elif output == "upgrade":
                        tower.upgrade()
                        

