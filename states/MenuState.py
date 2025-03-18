from states.State import *
from entities.Button import *
from states.MenuButtonData import *

class MenuState(State):
    def __init__(self, game, x=0, y=0):
        super().__init__(game)
        self.buttons = []
        self.background = None
        self.x = x
        self.y = y

    def create_buttons(self, game):

        num_buttons = len(self.button_data)

        total_button_height = num_buttons * BUTTONHEIGHT + (num_buttons - 1) * BUTTONSPACING
        start_y = self.y + (SCREEN_HEIGHT - total_button_height) // 2 
        x_position = (SCREEN_WIDTH  - BUTTONWIDTH )// 2

        for index, (text, output) in enumerate(self.button_data):
            y_position = start_y + index * (BUTTONHEIGHT + BUTTONSPACING)
            button = MenuButton(x_position, y_position, BUTTONWIDTH, BUTTONHEIGHT, text, output, game)
            self.buttons.append(button)

    def update(self):
        for button in self.buttons:
            output = button.handle_event()
            if output:
                return output
        return self.state

    def render(self, screen):
       # screen.blit(self.background, self.x, self.y)
        for button in self.buttons:
            #print("button rendered")
            button.render(screen)


class MainMenuState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "mainmenu"
        self.button_data = MAINMENUBUTTONDATA
        self.create_buttons(game)

class PauseState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "pause"
        self.button_data = PAUSEMENUBUTTONDATA
        self.create_buttons(game)

class GameOverState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "gameover"
        self.button_data = GAMEOVERMENUDATA
        self.create_buttons(game)       

class OptionsState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "options"
        self.button_data = OPTIONSMENUDATA
        self.create_buttons(game)     

class MapSelectState(MenuState):
    def __init__(self, game, gamestate):
        super().__init__(game)
        self.gamestate = gamestate
        self.state = "mapselect"
        self.button_data = MAPSELECTMENUBUTTONDATA
        self.create_buttons(game)     

    def update(self):
        output =  super().update()
        if output == "mainmenu":
            return output
        elif output != self.state:
            self.gamestate.grid_manager.load_map_data(output)
            return "playing"
        return self.state


