from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, game):
        self.game = game
    
    def enter(self):
        pass

    def exit(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass
