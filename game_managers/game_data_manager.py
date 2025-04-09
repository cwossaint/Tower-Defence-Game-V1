from constants.global_constants import *
import pygame
import time

class GameDataManager():
    def __init__(self) -> None:
        # Initialize the font for rendering text and some default game data
        self.font = pygame.font.SysFont("Arial", 20)
        self.message_font = pygame.font.SysFont("Arial", 50)
        self.cash = 50  # Starting cash
        self.lives = 100  # Starting lives
        self.wave = 0  # Starting wave
        self.game_message = ""  # Message to be displayed on screen
        self.current_time = 0  # Track the current time for message clearing
        self.message_clear_time = 3  # Time in seconds before message is cleared
        self.last_message_change_time = 0  # Track the last time a message was set

    def add_cash(self, amount):
        # Add a specified amount of cash
        self.cash += amount

    def remove_cash(self, amount):
        # Remove a specified amount of cash
        self.cash -= amount

    def remove_lives(self, amount):
        # Subtract a specified amount of lives
        self.lives -= amount

    def next_wave(self):    
        # Increment the wave number
        self.wave += 1

    def set_message(self, message):
        # Set a new game message and reset the timer for message clearing
        self.game_message = message
        self.last_message_change_time = time.time()

    def reset_data(self):
        # Reset game data like wave, lives, and cash to initial values
        self.wave = 1  # Reset wave to 1 (next wave)
        self.lives = 100  # Reset lives to 100
        self.cash = 20  # Reset cash to 20

    def game_over(self):
        # Check if the game is over (lives <= 0)
        return self.lives <= 0
    
    def update(self):
        # Update the current time and check if the message should be cleared
        self.current_time = time.time()
        if self.current_time - self.last_message_change_time >= self.message_clear_time:
            # Clear the message after the specified time
            self.set_message("")

    def render(self, screen):
        # Render game information (cash, lives, wave) and the game message on the screen
        cash_text = self.font.render("Money: $" + str(self.cash), True, WHITE)
        screen.blit(cash_text, (0, 20))  # Render cash in the top left corner
        
        lives_check = self.font.render("Lives: " + str(self.lives), True, WHITE)
        screen.blit(lives_check, (0, 0))  # Render lives in the top left corner (below cash)
        
        wave_text = self.font.render("Wave: " + str(self.wave), True, WHITE)
        screen.blit(wave_text, (650, 0))  # Render wave number at the top right
        
        game_message = self.message_font.render(self.game_message, True, BLUE)
        message_rect = game_message.get_rect()
        messagex, messagey = (message_rect.width//2), (SCREEN_HEIGHT//2 - message_rect.height//2) # centre message on game map
        screen.blit(game_message, (messagex, messagey))  # Render the game message in the center of the screen

    def reset(self):
        # Reset the lives, cash, and wave data to default values
        self.lives = 100
        self.cash = 50
        self.wave = 0
