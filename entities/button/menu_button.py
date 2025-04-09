from entities.button.base_button_class import Button

# MenuButton class inherits from the base Button class
class MenuButton(Button):

    # Class-level list to keep track of all MenuButton instances
    all_menu_buttons = []

    def __init__(self, x, y, width, height, text, action, game):
        # Call the constructor of the base Button class
        super().__init__(x, y, width, height, text, action, game)
        
        # Add this button instance to the shared list
        self.all_menu_buttons.append(self)
