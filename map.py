import pygame
from constants import *

class Map():
    def __init__(self, game, grid_manager) -> None:
        self.game = game
        self.grid_manager = grid_manager

    def render(self, screen):
        #screen.blit(self.sprite, (0, 0))
        for x in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line(screen, (255,255,255), (x, 0), (x, GRID_SIZE), 1)
        for y in range(0, GRID_SIZE + 1, TILE_SIZE):
            pygame.draw.line(screen, (255,255,255), (0, y), (GRID_SIZE, y), 1)
        self.highlight_tile(screen)

    def highlight_tile(self, screen):
        x, y = self.game.mouse.get_position()
        row, col = self.grid_manager.screen_to_grid(x, y)
        nx, ny = self.grid_manager.grid_to_screen(row, col)
        print(nx, ny)
        pygame.draw.rect(screen, (255, 0, 0), (nx, ny, TILE_SIZE, TILE_SIZE), 5)
