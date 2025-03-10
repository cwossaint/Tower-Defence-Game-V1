import pygame

class Game():

    def __init__(self):
        self.clock = pygame.time.Clock() 

    def run(self, screen):

        running = True
        while running:

            for event in pygame.event.get():
             
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


game = Game()