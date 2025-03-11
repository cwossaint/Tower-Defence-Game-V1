from grid import *

class Map():
    def __init__(self) -> None:
        pass

    def screen_to_grid(x, y):
        row = y//map_grid.tile_size
        col = x//map_grid.tile_size
        return row, col

    def grid_to_screen(row, col):
        y = row * map_grid.tile_size
        x = col * map_grid.tile_size
        return x, y

    def render():
        pass

    def select_tile(row, col):
        return map_grid.array[row][col]

    def highlight_tile():
        pass
