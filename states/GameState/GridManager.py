from entities.tower import *
from constants import *
from level_data import *
import copy

class GridManager():
    def __init__(self, game, guimanager, game_data) -> None:
        self.towers = { "dart": Dart,
                        "glue": Glue,
                        "cannon": Cannon,
                        "boomerang": Boomerang }
        
        self.arraysdict = {"map1" : LEVEL1MAPARRAY, 
                       "map2": LEVEL2MAPARRAY}
        self.array = None
        self.game = game
        self.game_data = game_data
        self.guimanager = guimanager
        self.selected_placed_tower = None

    def load_map_data(self, chosenmap):
        self.array = copy.deepcopy(self.arraysdict.get(chosenmap))

    def is_tile_valid(self, row, col):
        return self.array[row][col] == 0
    
    def get_tile_value(self, row, col):
        return self.array[row][col]
    
    def place_tower(self, row, col, chosentower):
        x, y = self.grid_to_screen(row, col)
        tower_obj = chosentower(x, y)
        self.set_tile_value(row, col, tower_obj)

    def sufficient_cash(self, chosentower):
        if not chosentower.cost > self.game_data.cash:
             self.game_data.remove_cash(chosentower.cost)
             return True
        self.game_data.set_message("insufficient funds")
        return False

    def update(self): 
        if self.game.mouse.is_pressed():
            x, y = self.game.mouse.get_position()
            row, col = self.screen_to_grid(x, y)

            if self.guimanager.selected_tower:
                if self.is_tile_valid(row, col):
                    tower_type = self.towers.get(self.guimanager.selected_tower)
                    if tower_type:
                        if self.sufficient_cash(tower_type):
                            self.place_tower(row, col, tower_type)
                            self.guimanager.unselect_tower()
            else: 
                tile_value = self.get_tile_value(row, col)
                if not isinstance(tile_value, int):
                    if not self.selected_placed_tower:
                        self.select_tower(row, col)
                if self.selected_placed_tower != tile_value:
                    self.unselect_tower()

    def unselect_tower(self):
        self.selected_placed_tower = None

    def select_tower(self, row, col):
        self.selected_placed_tower = self.get_tile_value(row, col)
                
    def set_tile_value(self, row, col, value):
        self.array[row][col] = value

    def screen_to_grid(self, x, y):
        row = y//TILE_SIZE
        col = x//TILE_SIZE
        return row, col

    def grid_to_screen(self, row, col):
        y = row * TILE_SIZE
        x = col * TILE_SIZE
        return x, y
    
    def select_tile(self):
        if self.game.mouse.is_pressed():
            x, y = self.game.mouse.get_position()
            row, col = self.screen_to_grid(x, y)
            return row, col
        
    def get_array(self):
        return self.array
        
    def reset(self):
        self.array = None