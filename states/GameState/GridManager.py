from entities.tower import *
from constants import *
from level_data import *

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

    def load_map_data(self, chosenmap):
        self.array = self.arraysdict.get(chosenmap)

    def is_tile_valid(self, row, col):
        return self.array[row][col] == 0
    
    def get_tile_value(self, row, col):
        return self.array[row][col]

    def update(self):
        pass
    
    def place_tower(self, row, col, chosentower):
        x, y = self.grid_to_screen(row, col)
        chosentower(x, y)
        
    def sufficient_cash(self, chosentower):
        if not chosentower.cost > self.game_data.cash:
             self.game_data.remove_cash(chosentower.cost)
             return True
        self.game_data.set_message("insufficient funds")
        return False

    def update(self): 
        if self.guimanager.selected_tower:
            if self.game.mouse.is_pressed():
                x, y = self.game.mouse.get_position()
                row, col = self.screen_to_grid(x, y)
                if self.is_tile_valid(row, col):
                    tower = self.towers.get(self.guimanager.selected_tower)
                    if tower:
                        if self.sufficient_cash(tower):
                            self.place_tower(row, col, tower)
                            self.update_tower_placement(row, col, tower)
                            self.guimanager.unselect_tower()

                
    def update_tower_placement(self, row, col, tower):
        self.array[row][col] = tower

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
        
