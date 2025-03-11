class Grid():
    def __init__(self) -> None:
        self.tile_size = 75
        self.grid_size = 10
        self.arraysdict  = {}
        self.array = None

    def load_map_data(self, chosenmap):
        self.array = self.arraysdict.get(chosenmap)

    def get_grid_value(self, row, col):
        return self.array[row][col]

    def set_grid_value(self, row, col, value):
        self.array[row][col] = value

    def is_grid_value(self, row, col):
        if self.array[row][col] == 0:
            return True
        return False

    def update_tower_placement(self, row, col, tower):
        self.array[row][col] = tower

map_grid = Grid()