from entities.Button import *

class GUIManager:
    def __init__(self):
        self.buttons = []
        self.selected_tower = None
        pass
    
    def create_buttons(self):
        pass

    def update(self):
       
        pass

    def unselect_tower(self):
        self.selected_tower = None
    
    def select_tower(self):
        for button in self.buttons:
            tower = button.handle_event()
            if tower:
                self.selected_tower = tower
            
    def render(self, screen):
        for button in self.buttons:
            button.render(screen)
        
guimanager = GUIManager()