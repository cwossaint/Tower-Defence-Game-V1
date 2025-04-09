from states.menu_states.main_menu_state_class import *
from states.menu_states.pause_menu_state_class import *
from states.menu_states.game_over_menu_state_class import *
from states.menu_states.options_menu_state_class import *
from states.menu_states.map_select_menu_state_class import *
from states.game_state import *

class StateManager():
    def __init__(self, game):
        # Current state name (used for transitions and logic)
        self.current_state = "mainmenu"

        # Next state to transition to after update (can be changed by current state's logic)
        self.next_state = "mainmenu"

        # Dictionary storing instances of all game states
        self.states = {}

        # Reference to the main game object
        self.game = game

        # Instantiate all game and menu states
        self.initialise_states(game)

        # Store the actual current state instance (not just name)
        self.current_state_instance = self.states.get(self.current_state)

    def initialise_states(self, game):
        """Initializes all the states the game can transition to."""

        # Create instances of each game/menu state
        mainmenu = MainMenuState(game)
        pause = PauseState(game)
        gameover = GameOverState(game)
        playing = GameState(game)
        options = OptionsState(game)
        mapselect = MapSelectState(game, playing)

        # Store each state in the dictionary with its associated name
        self.states["mainmenu"] = mainmenu
        self.states["options"] = options
        self.states["pause"] = pause
        self.states["mapselect"] = mapselect
        self.states["gameover"] = gameover
        self.states["playing"] = playing

    def update_state(self):
        """
        Switch to a new state if `next_state` has changed.
        Also resets the playing state when returning to main menu.
        """
        if self.next_state in self.states or self.next_state == "quit":
            # If transitioning to a different state
            if self.next_state != self.current_state:
                # Reset the game if going back to main menu
                if self.next_state == "mainmenu":
                    self.states["playing"].reset()

                # Update the current state and instance reference
                self.current_state = self.next_state
                self.current_state_instance = self.states.get(self.current_state)
        else:
            # If invalid next_state, revert to current
            self.next_state = self.current_state

    def update(self):
        """
        Updates the current state logic and stores the result
        (e.g. whether the player clicked to pause, go to menu, etc.).
        """
        if self.current_state_instance:
            self.next_state = self.current_state_instance.update()

    def render(self, screen):
        """
        Clears the screen and renders the current state's visuals.
        """
        if self.current_state_instance:
            screen.fill(BLACK)
            self.current_state_instance.render(screen)

    def should_quit(self):
        """
        Returns True if the game should quit, otherwise False.
        """
        return self.current_state == "quit"
