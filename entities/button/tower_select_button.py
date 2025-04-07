from entities.button.base_button_class import Button

class TowerSelectButton(Button):

    all_tower_select_buttons = []

    def __init__(self, x, y, width, height, text, action, game):
        super().__init__(x, y, width, height, text, action, game)
        self.all_tower_select_buttons.append(self)
    


