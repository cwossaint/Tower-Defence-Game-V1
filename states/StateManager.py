from states.MenuState import *
from states.GameState import *

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
        mapselect = MapSelect(game)
        gameover = GameOverState(game)
        playing = GameState(game)
        options = OptionsState(game)

        self.states["mainmenu"] = mainmenu
        self.states["options"] = options
        self.states["pause"] = pause
        self.states["mapselect"] = mapselect
        self.states["gameover"] = gameover
        self.states["playing"] = playing

    def update(self):
        if self.next_state != self.current_state:
            self.current_state = self.next_state
            self.current_state_instance = self.states.get(self.current_state)
        print(self.current_state)
        #print(self.current_state_instance)
        print(self.current_state_instance)

    def handle_event(self):
        if self.current_state_instance:
            self.next_state = self.current_state_instance.handle_event()
            #print("handled event")

    def render(self, screen):
        if self.current_state_instance:
            screen.fill(BLACK)
            self.current_state_instance.render(screen)
            #print("rendered")

    def should_quit(self):
        if self.current_state == "quit":
            print("quit")
            return True
        return False