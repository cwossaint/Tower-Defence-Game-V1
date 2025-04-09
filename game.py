import pygame
from states.state_manager import StateManager
from constants.global_constants import *

class Game():

    def __init__(self):
        # Initialize the game clock to manage frame rate
        self.clock = pygame.time.Clock()

        # Create an instance of the StateManager to control game state transitions
        self.StateManager = StateManager(self)

        # Font for displaying FPS on the screen
        self.font = pygame.font.SysFont("Arial", 20)

    def run(self, screen):
        """
        Main game loop where the game runs until the player quits.
        - Updates the state (transition logic).
        - Handles events (such as quitting the game).
        - Renders the game screen.
        - Tracks and displays the frame rate (FPS).
        """
        running = True
        while running:
            # Update the state logic (transitions, state-specific updates)
            self.StateManager.update_state()

            # Update the current state (e.g. gameplay, menu)
            self.StateManager.update()

            # Event handling (such as quit events)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.StateManager.should_quit():
                    # Exit the loop if user clicks the close button or if the game signals to quit
                    running = False

            # Render the current state's visual (UI, gameplay, menus, etc.)
            self.StateManager.render(screen)

            # Calculate and render FPS to track performance
            fps_text = self.font.render("fps: " + str(self.clock.get_fps()//1), True, WHITE)
            screen.blit(fps_text, (0, 725))

            # Update the display with everything drawn so far
            pygame.display.flip()

            # Limit the frame rate to 60 frames per second
            self.clock.tick(60)

        # Quit the game properly once the loop ends
        pygame.quit()
