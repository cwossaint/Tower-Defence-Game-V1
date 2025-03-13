from GUIManager import *
from constants import *

class GridManager():
    def __init__(self, game) -> None:
        self.arraysdict  = {}
        self.towers = {}
        self.array = None
        self.game = game

    def load_map_data(self, chosenmap):
        self.array = self.arraysdict.get(chosenmap)

    def is_tile_valid(self, row, col):
        return self.array[row][col] == 0

    def update(self):
        
        pass
    
    def place_tower(self, row, col, tower_type):
        
        pass

    def handle_event(self):
        if guimanager.selected_tower and self.game.mouse.is_pressed():
            x, y = self.game.mouse.get_position()
            row, col = self.screen_to_grid(x, y)
            if self.is_tile_valid(row, col):
                tower = self.towers.get(guimanager.selected_tower)
                if tower:
                    self.place_tower(row, col, tower)
                    self.update_tower_placement(row, col, tower)
                    guimanager.unselect_tower()
                
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
