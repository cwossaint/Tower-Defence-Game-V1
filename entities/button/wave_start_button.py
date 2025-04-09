from entities.button.base_button_class import Button

# WaveStartButton class inherits from the base Button class
class WaveStartButton(Button):

    # Class-level list to store all WaveStartButton instances
    wave_start_buttons = []

    def __init__(self, x, y, width, height, text, action, game):
        # Initialize the Button using the parent class constructor
        super().__init__(x, y, width, height, text, action, game)
        
        # Add this instance to the class-level list
        self.wave_start_buttons.append(self)
