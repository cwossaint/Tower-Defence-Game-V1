import pygame
from constants import *

class Map():
    def __init__(self, game, grid_manager) -> None:
        self.game = game
        self.grid_manager = grid_manager

    def render(self, screen):
        #screen.blit(self.sprite, (0, 0))
        for x in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line(screen, (139, 100, 64), (x, 0), (x, GRID_SIZE), 1)
        for y in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line(screen, (139, 100, 64), (0, y), (GRID_SIZE, y), 1)

    def highlight_tile(self, screen):
        x, y = self.game.mouse.get_position()
        row, col = self.grid_manager.screen_to_grid(x, y)
        nx, ny = self.grid_manager.grid_to_screen(row, col)
        pygame.draw.rect(screen, (255, 0, 0), (nx, ny, TILE_SIZE, TILE_SIZE), 5)

    def draw_map_obstacles(self, screen):
        for row in range(len(self.grid_manager.array)):
            for col in range(len(self.grid_manager.array[row])):
                grid_value = self.grid_manager.get_tile_value(row, col)
                if grid_value == 1:
                    colour = (181, 101, 29)
                elif grid_value == 0:
                    colour = (101, 67, 33) 
                elif grid_value == 2:
                    colour = (34, 139, 34)
                else:
                    pass
                x, y = self.grid_manager.grid_to_screen(row, col)
                pygame.draw.rect(screen, colour, (x, y, TILE_SIZE, TILE_SIZE))
 