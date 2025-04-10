import pygame
from constants.global_constants import *

#manages the rendering for the game map
class MapManager():
    def __init__(self, game, grid_manager) -> None:
        # Initialize MapManager with references to the game and grid_manager
        self.game = game
        self.grid_manager = grid_manager

    def render(self, screen):
        # This function renders the grid lines for the map
        # Loop through the grid and draw horizontal and vertical lines
        for x in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line(screen, BROWN, (x, 0), (x, GRID_SIZE), 1)  # Vertical lines
        for y in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line(screen, BROWN, (0, y), (GRID_SIZE, y), 1)  # Horizontal lines

    def highlight_tile(self, screen):
        # This function highlights the tile under the mouse cursor
        # Get the mouse position
        x, y = pygame.mouse.get_pos()
        # Convert screen coordinates to grid coordinates
        row, col = self.grid_manager.screen_to_grid(x, y)
        # Convert grid coordinates to screen coordinates to draw the rectangle
        nx, ny = self.grid_manager.grid_to_screen(row, col)
        # Draw a red rectangle around the tile to highlight it
        pygame.draw.rect(screen, (255, 0, 0), (nx, ny, TILE_SIZE, TILE_SIZE), 5)

# This function draws obstacles on the map (such as walls or paths)
    def draw_map_obstacles(self, screen):
        # iterate through each row and column in the grid
        for row in range(len(self.grid_manager.array)):
            for col in range(len(self.grid_manager.array[row])):
                grid_value = self.grid_manager.get_tile_value(row, col)
                # Set the color based on the grid value (e.g., obstacles, paths)
                if grid_value == 1 or grid_value == 4:
                    colour = LIGHT_BROWN  # Path
                elif grid_value == 3:
                    colour = GRAY  # Base
                elif grid_value == 2:
                    colour = DARK_GREEN  # map obstacle
                else:  
                    colour = DARK_BROWN  # Empty tiles or tower tiles
                if colour:
                    # Convert grid coordinates to screen coordinates to draw the rectangle
                    x, y = self.grid_manager.grid_to_screen(row, col)
                    # Draw the tile with the corresponding color
                    pygame.draw.rect(screen, colour, (x, y, TILE_SIZE, TILE_SIZE))
