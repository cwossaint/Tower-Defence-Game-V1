from game_managers.grid_manager import *


#responsible for finding the path in which enemies should follow for a given map
class PathfindingManager():
    def __init__(self, grid_manager):
        # Initialize PathfindingManager with a reference to grid_manager
        self.grid_manager = grid_manager
        self.map_array = None  # To store the map layout
        self.directions = []  # To store the calculated directions for the path
        self.current_point = None  # To track the current position during pathfinding

    def generate_path(self):
        # This function generates the path from the start to the end point
        self.map_array = self.grid_manager.get_array()  # Get the grid layout
        start_point = self.locate_start_point()  # Find the starting point
        self.current_point = start_point  # Set the current point as the start point
        current_direction = None  # No direction at the beginning

        path = True
        while path:
            # Find the next point in the path
            next_direction = self.locate_next_point(current_direction)
            if next_direction:
                # If a valid next point is found, add it to the directions list
                self.directions.append(next_direction)
                current_direction = next_direction  # Update the current direction
            else:
                # If no next point is found, the path is complete
                path = False
        return self.directions  # Return the list of directions

    def locate_start_point(self):
        # This function locates the start point (denoted by 4 in the grid)
        for row_index, row in enumerate(self.map_array):
            if 4 in row:  # Check if 4 is in the row
                col_index = row.index(4)  # Get the column index of the start point
                return (row_index, col_index)  # Return the row and column as a tuple
            
    def locate_end_point(self):
        # This function locates the end point (denoted by 3 in the grid)
        for row_index, row in enumerate(self.map_array):
            if 3 in row:  # Check if 3 is in the row
                col_index = row.index(3)  # Get the column index of the end point
                return (row_index, col_index)  # Return the row and column as a tuple

    def locate_next_point(self, current_direction):
        # This function locates the next valid point to move to
        row, col = self.current_point  # Get the current position

        # Check if we can move right
        if col + 1 < len(self.map_array[row]):  # Ensure we are within bounds
            if self.map_array[row][col + 1] == 1 and current_direction != "left":  # Check if the tile is walkable and not backtracking
                self.current_point = (row, col + 1)  # Update the current position
                return "right"  # Return the direction moved

        # Check if we can move left
        if col - 1 >= 0:  # Ensure we are within bounds
            if self.map_array[row][col - 1] == 1 and current_direction != "right":  # Check if the tile is walkable and not backtracking
                self.current_point = (row, col - 1)  # Update the current position
                return "left"  # Return the direction moved

        # Check if we can move down
        if row + 1 < len(self.map_array):  # Ensure we are within bounds
            if self.map_array[row + 1][col] == 1 and current_direction != "up":  # Check if the tile is walkable and not backtracking
                self.current_point = (row + 1, col)  # Update the current position
                return "down"  # Return the direction moved

        # Check if we can move up
        if row - 1 >= 0:  # Ensure we are within bounds
            if self.map_array[row - 1][col] == 1 and current_direction != "down":  # Check if the tile is walkable and not backtracking
                self.current_point = (row - 1, col)  # Update the current position
                return "up"  # Return the direction moved

        return None  # Return None if no valid direction is found

    def reset(self):
        # This function resets the pathfinding manager by clearing the map and directions
        self.map_array = None
        self.directions = []  # Clear the directions list
        self.current_point = None  # Reset the current position
