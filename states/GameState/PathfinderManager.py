from states.GameState.GridManager import *

class PathfindingManager():
    def __init__(self, grid_manager):
        self.grid_manager = grid_manager
        self.map_array = None
        self.directions = []
        self.current_point = None

    def generate_path(self):
        self.map_array = self.grid_manager.get_array()
        start_point = self.locate_start_point()
        self.current_point = start_point
        current_direction = None

        path = True
        while path:
            next_driection = self.locate_next_point(current_direction)
            if next_driection:
                self.directions.append(next_driection)
                current_direction = next_driection
            else: 
                path = False
        return self.directions
        

    def locate_start_point(self):
        for row_index, row in enumerate(self.map_array):
            if 4 in row:
                col_index = row.index(4) 
                return (row_index, col_index)  
            
    def locate_end_point(self):
        for row_index, row in enumerate(self.map_array):
            if 3 in row:
                col_index = row.index(3) 
                return (row_index, col_index)  

    def locate_next_point(self, current_direction):
        row, col = self.current_point

        # Check right
        if col + 1 < len(self.map_array[row]):  
            if self.map_array[row][col + 1] == 1 and current_direction != "left":
                self.current_point = (row, col + 1)  
                return "right"

        # Check left
        if col - 1 >= 0:
            if self.map_array[row][col - 1] == 1 and current_direction != "right":
                self.current_point = (row, col - 1) 
                return "left"

        # Check down
        if row + 1 < len(self.map_array):
            if self.map_array[row + 1][col] == 1 and current_direction != "up":
                self.current_point = (row + 1, col)  
                return "down"

        # Check up
        if row - 1 >= 0:
            if self.map_array[row - 1][col] == 1 and current_direction != "down":
                self.current_point = (row - 1, col) 
                return "up"

        return None

    def reset(self):
        self.map_array = None
        self.directions = []
        self.current_point = None