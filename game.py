import pygame
from states.StateManager import *
from Mouse import *

class Game():

    def __init__(self):
        self.clock = pygame.time.Clock() 
        self.mouse = Mouse()
        self.StateManager = StateManager(self)
        self.font = pygame.font.SysFont("Arial", 20)

    def run(self, screen):

        running = True
        while running:

            self.StateManager.update_state()
            self.StateManager.update()

            for event in pygame.event.get():
                self.mouse.update()
                if event.type == pygame.QUIT or self.StateManager.should_quit():
                    running = False

            self.StateManager.render(screen)

            fps_text = self.font.render("fps: " + str(self.clock.get_fps()), True, WHITE)
            screen.blit(fps_text, (0, 730))

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
