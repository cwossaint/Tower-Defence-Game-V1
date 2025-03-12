from GridManager import *
import pygame

class Map():
    def __init__(self) -> None:
        pass

    def screen_to_grid(x, y):
        row = y//grid_manager.tile_size
        col = x//grid_manager.tile_size
        return row, col

    def grid_to_screen(row, col):
        y = row * grid_manager.tile_size
        x = col * grid_manager.tile_size
        return x, y

    def render(self, screen):
        screen.blit(self.sprite, (0, 0))
        for x in range(0, grid_manager.grid_size + 1, grid_manager.tile_size):
            pygame.draw.line((screen, (0,0,0)), (x, 0), (x, grid_manager.grid_size), 1)
        for y in range(0, grid_manager.grid_size + 1, grid_manager.tile_size):
            pygame.draw.line((screen, (0,0,0)), (0, y), (grid_manager.grid_size, y), 1)
        self.highlight_tile(screen)

    def select_tile(row, col):
        return grid_manager.array[row][col]

    def highlight_tile(self, screen):
        x, y = self.game.mouse.get_position()
        row, col = self.screen_to_grid(x, y)
        nx, ny = self.grid_to_screen(row, col)
        pygame.draw.rect((screen, (255, 0, 0)), (nx * grid_manager.tile_size, ny * grid_manager.tile_size, grid_manager.tile_size, grid_manager.tile_size), 5)
