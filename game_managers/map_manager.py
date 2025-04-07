import pygame
from constants.global_constants import *

class MapManager():
    def __init__(self, game, grid_manager) -> None:
        self.game = game
        self.grid_manager = grid_manager

    def render(self, screen):
        #screen.blit(self.sprite, (0, 0))
        for x in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line(screen, BROWN, (x, 0), (x, GRID_SIZE), 1)
        for y in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line(screen, BROWN, (0, y), (GRID_SIZE, y), 1)

    def highlight_tile(self, screen):
        x, y = pygame.mouse.get_pos()
        row, col = self.grid_manager.screen_to_grid(x, y)
        nx, ny = self.grid_manager.grid_to_screen(row, col)
        pygame.draw.rect(screen, (255, 0, 0), (nx, ny, TILE_SIZE, TILE_SIZE), 5)

    def draw_map_obstacles(self, screen):
        for row in range(len(self.grid_manager.array)):
            for col in range(len(self.grid_manager.array[row])):
                grid_value = self.grid_manager.get_tile_value(row, col)
                if grid_value == 1 or grid_value == 4:
                    colour = LIGHT_BROWN
                elif grid_value == 3:
                    colour = GRAY
                elif grid_value == 2:
                    colour = DARK_GREEN
                else: # 0 and towers
                    colour = DARK_BROWN
                if colour:
                    x, y = self.grid_manager.grid_to_screen(row, col)
                    pygame.draw.rect(screen, colour, (x, y, TILE_SIZE, TILE_SIZE))
    