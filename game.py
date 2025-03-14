import pygame
from states.StateManager import *
from Mouse import *

class Game():

    def __init__(self):
        self.clock = pygame.time.Clock() 
        self.mouse = Mouse()
        self.StateManager = StateManager(self)

    def run(self, screen):

        running = True
        while running:

            self.StateManager.update()
            self.StateManager.handle_event()

            for event in pygame.event.get():

                self.mouse.update()

                

                if event.type == pygame.QUIT or self.StateManager.should_quit():
                    running = False

            self.StateManager.render(screen)

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
