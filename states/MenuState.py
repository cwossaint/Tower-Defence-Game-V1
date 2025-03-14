from states.State import *
from entities.Button import *
from states.GameState import *

class MenuState(State):
    def __init__(self, game, x=0, y=0):
        super().__init__(game)
        self.buttons = []
        self.background = None
        self.x = x
        self.y = y
        self.create_buttons(game)

    def create_buttons(game):
        pass

    def handle_event(self):
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

    def create_buttons(self, game):
        QuitGameButton = MenuButton(500, 100, 200, 100, "Quit Game", "quit", game)
        PlayGameButton = MenuButton(500, 350, 200, 100, "Play", "mapselect", game)
        OptionsGameButton = MenuButton(500, 600, 200, 100, "Options", "options", game)

        self.buttons.append(QuitGameButton)
        self.buttons.append(PlayGameButton)
        self.buttons.append(OptionsGameButton)

class PauseState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "pause"

    def create_buttons(self, game):
        ResumeButton = MenuButton(500, 100, 200, 100, "Resume", "playing", game)
        BackToMainMenuButton = MenuButton(500, 350, 200, 100, "Back to Main Menu", "mainmenu", game)

        self.buttons.append(ResumeButton)
        self.buttons.append(BackToMainMenuButton)

class GameOverState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "gameover"

    def create_buttons(self, game):
        BackToMainMenuButton = MenuButton(500, 100, 200, 100, "Back to Main Menu", "mainmenu", game)
        self.buttons.append(BackToMainMenuButton)

class OptionsState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "options"

    def create_buttons(self, game):
        BackToMainMenuButton = MenuButton(500, 100, 200, 100, "Back to Main Menu", "mainmenu", game)
        QuitGameButton = MenuButton(500, 350, 200, 100, "Quit Game", "quit", game)

        self.buttons.append(QuitGameButton)
        self.buttons.append(BackToMainMenuButton)

class MapSelectState(MenuState):
    def __init__(self, game, gamestate):
        super().__init__(game)
        self.gamestate = gamestate
        self.state = "mapselect"

    def create_buttons(self, game):
        Map1Button = MenuButton(500, 100, 200, 100, "Map 1", "map1", game)
        Map2Button = MenuButton(500, 300, 200, 100, "Map 2", "map2", game)
        BackToMainMenuButton = MenuButton(500, 500, 200, 100, "Back to Main Menu", "mainmenu", game)
        
        self.buttons.append(Map1Button)
        self.buttons.append(Map2Button)
        self.buttons.append(BackToMainMenuButton)

    def handle_event(self):
        output =  super().handle_event()
        if output == "mainmenu":
            return output
        elif output != self.state:
            self.gamestate.grid_manager.load_map_data(output)
            return "playing"
        return self.state


