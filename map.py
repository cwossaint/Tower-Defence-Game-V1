from grid import *
import pygame

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

    def render(self, screen):
        screen.blit(self.sprite, (0, 0))
        for x in range(0, map_grid.grid_size + 1, map_grid.tile_size):
            pygame.draw.line((screen, (0,0,0)), (x, 0), (x, map_grid.grid_size), 1)
        for y in range(0, map_grid.grid_size + 1, map_grid.tile_size):
            pygame.draw.line((screen, (0,0,0)), (0, y), (map_grid.grid_size, y), 1)
        self.highlight_tile(screen)

    def select_tile(row, col):
        return map_grid.array[row][col]

    def highlight_tile(self, screen):
        x, y = self.game.mouse.get_position()
        row, col = self.screen_to_grid(x, y)
        nx, ny = self.grid_to_screen(row, col)
        pygame.draw.rect((screen, (255, 0, 0)), (nx * map_grid.tile_size, ny * map_grid.tile_size, map_grid.tile_size, map_grid.tile_size), 5)
