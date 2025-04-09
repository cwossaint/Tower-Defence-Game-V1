import pygame
from constants.global_constants import *
from game import *

if __name__ == "__main__":
    # Initialize all the pygame modules (graphics, sound, etc.)
    pygame.init()
    # Initialize the pygame mixer for sound functionality
    pygame.mixer.init()
    # Initialize the display module to set up the screen/window
    pygame.display.init()
    # Create the display window with the specified width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Set the title of the game window to "Jiggery Junction"
    pygame.display.set_caption('Jiggery Junction')
    # Create a new instance of the Game class
    game = Game()
    # Start the game by calling the run method, passing the screen for rendering
    game.run(screen)
