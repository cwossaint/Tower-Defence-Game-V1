from GridManager import *
import pygame
from constants import *

class Map():
    def __init__(self) -> None:
        pass

    def render(self, screen):
        screen.blit(self.sprite, (0, 0))
        for x in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line((screen, (0,0,0)), (x, 0), (x, GRID_SIZE), 1)
        for y in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line((screen, (0,0,0)), (0, y), (GRID_SIZE, y), 1)
        self.highlight_tile(screen)

    def highlight_tile(self, screen):
        x, y = self.game.mouse.get_position()
        row, col = grid_manager.screen_to_grid(x, y)
        nx, ny = grid_manager.grid_to_screen(row, col)
        pygame.draw.rect((screen, (255, 0, 0)), (nx * TILE_SIZE, ny * TILE_SIZE, TILE_SIZE, TILE_SIZE), 5)
