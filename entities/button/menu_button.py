from entities.button.base_button_class import Button

class MenuButton(Button):

    all_menu_buttons = []

    def __init__(self, x, y, width, height, text, action, game):
        super().__init__(x, y, width, height, text, action, game)
        self.all_menu_buttons.append(self)