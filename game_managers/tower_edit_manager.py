from entities.tower.base_tower_class import *
from constants.gui_constants import *
from constants.global_constants import *


#manages side panel buttons when a placed tower is selected. Handles upgrades and stats preview for selected tower 
class TowerEditGUIManager():
    def __init__(self, game, grid_manager, game_data):
        self.game = game  # Reference to the main game
        self.grid_manager = grid_manager  # Reference to the grid manager (used for tower placement)
        self.game_data = game_data  # Reference to the game data (used for managing cash, lives, etc.)
        self.tower_stats_text = []  # List to store current tower stats text
        self.upgrade_stats_text = []  # List to store stats for the next tower upgrade
        self.text_spacing = 30  # Space between lines of text for rendering
        self.button_data = TOWEREDITGUIBUTTONDATA  # Data for buttons (label, action, type)
        self.font = pygame.font.SysFont("Arial", 25)  # Font for displaying text
        self.buttons = []  # List to hold the buttons
        self.tower_radius_circle = None # Circle data for tower radius
        self.create_buttons()  # Initialize buttons when the class is created

    def create_buttons(self):
        num_buttons = len(self.button_data)  # Get the number of buttons

        # Calculate the total height of all buttons and their spacing
        total_button_height = num_buttons * GAMEBUTTONHEIGHT + (num_buttons - 1) * GAMEBUTTONSPACING
        # Start drawing buttons from the middle of the screen vertically
        start_y = 0 + (SCREEN_HEIGHT - total_button_height) // 2 
        # Position buttons to the right of the grid
        x_position = (SCREEN_WIDTH - GRID_SIZE - GAMEBUTTONWIDTH) // 2 + GRID_SIZE

        # Create each button based on the button data
        for index, (text, output, type) in enumerate(self.button_data):
            y_position = start_y + index * (GAMEBUTTONHEIGHT + GAMEBUTTONSPACING)
            button = type(x_position, y_position, GAMEBUTTONWIDTH, GAMEBUTTONHEIGHT, text, output, self.game)
            self.buttons.append(button)  # Add the button to the list

    def render(self, screen):

        #render selected tower radius circle
        tower_pos, tower_range = self.tower_radius_display
        pygame.draw.circle(screen, RED, tower_pos, tower_range, 5)

        #draw black rectangle under gui to hide overlapping tower radius display on side panel
        pygame.draw.rect(screen, BLACK, (GRID_SIZE, 0, (SCREEN_WIDTH-GRID_SIZE), SCREEN_HEIGHT))

        # Render all buttons
        for button in self.buttons:
            button.render(screen)
        
        # Render tower stats text
        current_y = 0 - self.text_spacing
        for item in self.tower_stats_text:
            current_y += self.text_spacing
            text = self.font.render(item, True, WHITE)
            screen.blit(text, (780, current_y))  # Draw tower stats at the specified position
        
        # Render upgrade stats text
        current_y = 500
        for item in self.upgrade_stats_text:
            current_y += self.text_spacing
            text = self.font.render(item, True, WHITE)
            screen.blit(text, (780, current_y))  # Draw upgrade stats at the specified position

    def update(self):
        # Check if a tower is selected
        if self.grid_manager.selected_placed_tower:
            tower = self.grid_manager.selected_placed_tower  # Get the selected tower

            self.tower_radius_display = ((tower.centrex, tower.centrey), tower.range)

            # Get stats for the current upgrade of the tower
            current_upgrade_stats = tower.upgrade_stats[tower.level]

            # Clear the previous stats and update with current tower stats
            self.upgrade_stats_text = []
            self.tower_stats_text = []

            self.tower_stats_text.append(str(tower.name))  # Add the tower's name
            for stat in current_upgrade_stats:
                self.tower_stats_text.append(str(stat) + ": " + str(current_upgrade_stats[stat]))

            # If there's another upgrade level available
            if not tower.level + 1 > len(tower.upgrade_stats):

                # Get stats for the next upgrade level
                next_upgrade_stats = tower.upgrade_stats[tower.level + 1]

                # Show the upgrade level
                self.upgrade_stats_text.append("level: " + str(tower.level) + "->" + str(tower.level + 1))

                # Show the stat changes for the next upgrade
                for stat in next_upgrade_stats:
                    if stat != "cost":  # Skip cost stat, we handle it separately
                        self.upgrade_stats_text.append(str(stat) + ": " + str(current_upgrade_stats[stat]) + "->" + str(next_upgrade_stats[stat]))

                # Show the cost for the upgrade
                upgrade_cost = next_upgrade_stats["cost"]
                self.upgrade_stats_text.append("cost: " + str(upgrade_cost))

            else:
                # If the tower has reached max level, display "Max Level"
                self.upgrade_stats_text.append("Max Level")

        # Update each button's state
        for button in self.buttons:
            output = button.update()  # Get the button's output after it is clicked
            if output:
                tower = self.grid_manager.selected_placed_tower  # Get the selected tower
                if output == "back":
                    self.grid_manager.selected_placed_tower = None  # Unselect tower when "back" is pressed
                elif output == "remove":
                    tower.remove_tower()  # Remove the tower
                    x, y = tower.x, tower.y  # Get the position of the tower
                    row, col = self.grid_manager.screen_to_grid(x, y)  # Convert screen coordinates to grid coordinates
                    self.grid_manager.set_tile_value(row, col, 0)  # Set the grid value to 0 (empty space)
                elif output == "upgrade":
                    # If there's an upgrade available, check if the player has enough cash
                    if not tower.level + 1 > len(tower.upgrade_stats):
                        if self.game_data.cash >= upgrade_cost:
                            self.game_data.remove_cash(upgrade_cost)  # Deduct the upgrade cost from cash
                            tower.upgrade()  # Perform the upgrade
                        else:
                            self.game_data.set_message("not enough money")  # Display message if not enough money
