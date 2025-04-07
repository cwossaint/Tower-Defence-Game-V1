from entities.button.base_button_class import Button

class WaveStartButton(Button):

    wave_start_buttons = []

    def __init__(self, x, y, width, height, text, action, game):
        super().__init__(x, y, width, height, text, action, game)
        self.wave_start_buttons.append(self)