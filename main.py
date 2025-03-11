import pygame
from game import *


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.display.init()
    screen = pygame.display.set_mode((1080, 750))
    pygame.display.set_caption('Jiggery Junction')
    game = Game()
    game.run(screen)

