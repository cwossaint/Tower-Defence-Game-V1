from states.State import *
from entities.Button import *

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
        screen.fill((0, 0, 0))
        for button in self.buttons:
            #print("button rendered")
            button.render(screen)


class MainMenuState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "mainmenu"

    def create_buttons(self, game):
        QuitGameButton = MenuButton(500, 100, 200, 100, "Quit Game", "quit", game)
        PlayGameButton = MenuButton(500, 350, 200, 100, "Play", "playing", game)
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

class MapSelect(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "mapselect"

    def create_buttons(self, game):
        QuitGameButton = MenuButton(500, 100, 200, 100, "Quit Game", "quit", game)
        PlayGameButton = MenuButton(500, 350, 200, 100, "Play", "playing", game)
        OptionsGameButton = MenuButton(500, 600, 200, 100, "Options", "options", game)

        self.buttons.append(QuitGameButton)
        self.buttons.append(PlayGameButton)
        self.buttons.append(OptionsGameButton)

class OptionsState(MenuState):
    def __init__(self, game):
        super().__init__(game)
        self.state = "options"

    def create_buttons(self, game):
        BackToMainMenuButton = MenuButton(500, 100, 200, 100, "Back to Main Menu", "mainmenu", game)
        QuitGameButton = MenuButton(500, 350, 200, 100, "Quit Game", "quit", game)

        self.buttons.append(QuitGameButton)
        self.buttons.append(BackToMainMenuButton)

