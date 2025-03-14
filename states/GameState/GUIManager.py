from entities.Button import *

class GUIManager:
    def __init__(self, game):
        self.buttons = []
        self.selected_tower = None
        self.game = game
        self.create_buttons()
    
    def create_buttons(self):
        
        glue_tower_button = TowerSelectButton(800, 50, 200, 100, "Glue", "glue", self.game)
        boomerang_tower_button = TowerSelectButton(800, 250, 200, 100, "Boomerang", "boomerang", self.game)
        dart_tower_button = TowerSelectButton(800, 450, 200, 100, "Dart", "dart", self.game)
        cannon_tower_button = TowerSelectButton(800, 650, 200, 100, "Cannon", "cannon", self.game)

        self.buttons.append(glue_tower_button)
        self.buttons.append(boomerang_tower_button)
        self.buttons.append(dart_tower_button)
        self.buttons.append(cannon_tower_button)

    def unselect_tower(self):
        self.selected_tower = None
    
    def update(self):
        for button in self.buttons:
            tower = button.handle_event()
            if tower:
                self.selected_tower = tower

            
    def render(self, screen):
        for button in self.buttons:
            button.render(screen)
