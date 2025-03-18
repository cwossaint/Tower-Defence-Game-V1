from constants import *

class GameData():
    def __init__(self) -> None:
        self.cash = 20
        self.lives = 100
        self.wave = 1

    def add_cash(self, amount):
        self.cash += amount

    def remove_cash(self, amount):
        self.cash -= amount

    def remove_lives(self, amount):
        self.lives -= amount

    def next_wave(self):    
        self.wave += 1

    def reset_data(self):
        self.wave = 1
        self.lives = 100
        self.cash = 20

    def render(self, screen):
        cash_text = self.font.render("Money: $" + str(self.cash), True, WHITE)
        screen.blit(cash_text, (0, 20))
        lives_check = self.font.render("Lives: " + str(self.lives), True, WHITE)
        screen.blit(lives_check, (0, 0))
        wave_text = self.font.render("Wave: " + str(self.wave), True, WHITE)
        screen.blit(wave_text, (700, 0))