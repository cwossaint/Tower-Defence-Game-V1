from entities.tower.dart_tower_class import *
from entities.tower.glue_tower_class import *
from entities.tower.cannon_tower_class import *
from entities.tower.boomerang_tower_class import *
from entities.tower.gatling_tower_class import *
import pygame
from constants.global_constants import *
from constants.level_data import *
import copy

#manages placing towers onto the map grid and selecting already placed towers on the map grid
class GridManager():
    def __init__(self, game, guimanager, game_data):
        # Initialize the GridManager with references to the game, GUI manager, and game data
        # Set up a dictionary to store the tower classes by their names
        self.towers = { "dart": Dart,
                        "glue": Glue,
                        "cannon": Cannon,
                        "boomerang": Boomerang,
                         "gatling" : Gatling }

        # Define the level maps (as arrays) for different maps
        self.arraysdict = {"map1" : LEVEL1MAPARRAY, 
                       "map2": LEVEL2MAPARRAY, 
                       "map3" : LEVEL3MAPARRAY}

        self.array = None  # The grid map for the currently selected level
        self.game = game  # Reference to the game object
        self.game_data = game_data  # Reference to game data (cash, lives, etc.)
        self.guimanager = guimanager  # Reference to the GUI manager
        self.selected_placed_tower = None  # Reference to the tower selected for interaction

    def load_map_data(self, chosenmap):
        # Load the map data for the chosen map by copying the map array
        self.array = copy.deepcopy(self.arraysdict.get(chosenmap))

    def is_tile_valid(self, row, col):
        # Check if a tile is valid (empty) by checking if its value in the array is 0
        try:
            return self.array[row][col] == 0
        except IndexError:
            print("invalid tile (out of bounds) for " + str(row) + str(col))
            return False
    
    def get_tile_value(self, row, col):
        # Get the value of the tile at a specific grid position (either a tower or an empty tile)
        try:
            return self.array[row][col]
        except IndexError:
            print("invalid tile (out of bounds) for " + str(row) + str(col))
            return None
    
    def place_tower(self, row, col, chosentower):
        # Place a tower at the specified grid position (row, col)
        x, y = self.grid_to_screen(row, col)
        tower_obj = chosentower(x, y)  # Create a tower object
        self.set_tile_value(row, col, tower_obj)  # Set the tile value to the tower object

    def sufficient_cash(self, chosentower):
        # Check if the player has enough cash to place the selected tower
        if not chosentower.cost > self.game_data.cash:
            self.game_data.remove_cash(chosentower.cost)  # Deduct cash if tower is placed
            return True
        self.game_data.set_message("insufficient funds")  # Display message if not enough cash
        return False

    def update(self): 
        # Update the grid manager on each frame
        if pygame.mouse.get_pressed()[0]:  # Check if the left mouse button is pressed
            x, y = pygame.mouse.get_pos()  # Get the current mouse position
            row, col = self.screen_to_grid(x, y)  # Convert mouse position to grid position

            if self.guimanager.selected_tower:
                # If a tower is selected, attempt to place it
                if self.is_tile_valid(row, col):  # Check if the tile is valid for placing a tower
                    tower_type = self.towers.get(self.guimanager.selected_tower)  # Get tower class by name
                    if tower_type:
                        if self.sufficient_cash(tower_type):  # Check if there's enough cash
                            self.place_tower(row, col, tower_type)  # Place the tower
                        self.guimanager.unselect_tower()  # Deselect the tower
                else:
                    self.guimanager.unselect_tower() # Unselect tower if it's an invalid tile
            else: 
                # If no tower is selected, handle selection of a tower
                tile_value = self.get_tile_value(row, col)
                if not isinstance(tile_value, int):
                    if not self.selected_placed_tower:
                        self.select_tower(row, col)  # Select the tower at the clicked tile
                if self.selected_placed_tower != tile_value:
                    self.unselect_tower()  # Deselect the tower if a new tower is clicked

    def unselect_tower(self):
        # Unselect the currently selected tower
        self.selected_placed_tower = None

    def select_tower(self, row, col):
        # Select the tower at the specified grid position (row, col)
        self.selected_placed_tower = self.get_tile_value(row, col)
                
    def set_tile_value(self, row, col, value):
        # Set the value (e.g., tower) at a specific grid position
        try:
            self.array[row][col] = value
        except IndexError:
            print("invalid tile (out of bounds) for " + str(row) + str(col))
           

    def screen_to_grid(self, x, y):
        # Convert screen coordinates to grid coordinates (row, col)
        row = y // TILE_SIZE
        col = x // TILE_SIZE
        return row, col

    def grid_to_screen(self, row, col):
        # Convert grid coordinates (row, col) to screen coordinates (x, y)
        y = row * TILE_SIZE
        x = col * TILE_SIZE
        return x, y
    
    def select_tile(self):
        # Detect which tile is selected based on mouse position (not used in this code snippet)
        if self.game.mouse.is_pressed():
            x, y = self.game.mouse.get_position()
            row, col = self.screen_to_grid(x, y)
            return row, col
        
    def get_array(self):
        # Return the current map array
        return self.array
        
    def reset(self):
        # Reset the array (grid map) for a fresh start
        self.array = None
