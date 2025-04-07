from states.menu_states.main_menu_state_class import *
from states.menu_states.pause_menu_state_class import *
from states.menu_states.game_over_menu_state_class import *
from states.menu_states.options_menu_state_class import *
from states.menu_states.map_select_menu_state_class import *
from states.game_state import *

class StateManager():

    def __init__(self, game):
        self.current_state = "mainmenu"
        self.next_state = "mainmenu"
        self.states = {}
        self.game = game
        self.initialise_states(game)
        self.current_state_instance = self.states.get(self.current_state)

    def initialise_states(self, game):

        mainmenu = MainMenuState(game)
        pause = PauseState(game)
        gameover = GameOverState(game)
        playing = GameState(game)
        options = OptionsState(game)
        mapselect = MapSelectState(game, playing)

        self.states["mainmenu"] = mainmenu
        self.states["options"] = options
        self.states["pause"] = pause
        self.states["mapselect"] = mapselect
        self.states["gameover"] = gameover
        self.states["playing"] = playing

    def update_state(self):
        if self.next_state in self.states or self.next_state == "quit":
            if self.next_state != self.current_state:
                if self.next_state == "mainmenu":
                    self.states["playing"].reset()
                self.current_state = self.next_state
                self.current_state_instance = self.states.get(self.current_state)
        else:
            self.next_state = self.current_state

    def update(self):
        if self.current_state_instance:
            self.next_state = self.current_state_instance.update()

    def render(self, screen):
        if self.current_state_instance:
            screen.fill(BLACK)
            self.current_state_instance.render(screen)

    def should_quit(self):
        if self.current_state == "quit":
            return True
        return False