import pygame

class Mouse:
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.clicked = pygame.mouse.get_pressed()[0]
        self.right_clicked = pygame.mouse.get_pressed()[2]  # Detect right-click

    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.clicked = pygame.mouse.get_pressed()[0]
        self.right_clicked = pygame.mouse.get_pressed()[2]

    def get_position(self):
        return (self.x, self.y)

    def is_pressed(self):
        return self.clicked

    def is_right_clicked(self):
        return self.right_clicked
