import pygame
from constants import *
from game import *


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Jiggery Junction')
    game = Game()
    game.run(screen)

#import cProfile


#def main():
   #pygame.init()
    #pygame.mixer.init()
    #pygame.display.init()
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #pygame.display.set_caption('Jiggery Junction')
    #game = Game()
    #game.run(screen)

#cProfile.run("main()", sort="cumtime")
