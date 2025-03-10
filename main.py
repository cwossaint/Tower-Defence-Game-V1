import pygame
from game import *


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.display.init()
    screen = pygame.display.set_mode((1080, 750))
    pygame.display.set_caption('Jiggery Junction')
    game.run(screen)




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