from entities.button.base_button_class import *
from constants.gui_constants import *
from constants.global_constants import *

class GUIManager:
    def __init__(self, game):
        # Initialize the GUI Manager with essential game data
        self.buttons = []  # List to store all buttons
        self.selected_tower = None  # Selected tower by the player (if any)
        self.selected_button = None # selected tower button by the player
        self.game = game  # The main game object
        self.wave_start = False  # Flag to track if the wave has started
        self.button_data = GAMEGUIPANELBUTTONDATA  # Button data configuration
        self.create_buttons()  # Call to create buttons when GUIManager is initialized
    
    def create_buttons(self):
        # Create buttons for the GUI based on the button data
        num_buttons = len(self.button_data)  # Number of buttons from the data

        # Calculate the total height needed for buttons, including spacing between them
        total_button_height = num_buttons * GAMEBUTTONHEIGHT + (num_buttons - 1) * GAMEBUTTONSPACING
        
        # Calculate the starting y-position for buttons to center them vertically
        start_y = 0 + (SCREEN_HEIGHT - total_button_height) // 2 
        
        # Calculate the x-position for the button panel to position it properly
        x_position = (SCREEN_WIDTH - GRID_SIZE - GAMEBUTTONWIDTH) // 2 + GRID_SIZE

        # Create each button from the button data
        for index, (text, output, type) in enumerate(self.button_data):
            # Calculate the y-position for each button
            y_position = start_y + index * (GAMEBUTTONHEIGHT + GAMEBUTTONSPACING)
            
            # Instantiate the button and append it to the buttons list
            button = type(x_position, y_position, GAMEBUTTONWIDTH, GAMEBUTTONHEIGHT, text, output, self.game)
            self.buttons.append(button)

    def unselect_tower(self):
        # Unselect the currently selected tower
        if self.selected_tower:
            self.selected_button.is_selected = False
            self.selected_tower = None
    
    def update(self):
        # Update all buttons, checking for any actions (button presses)
        for button in self.buttons:
            output = button.update()  # Update each button
            
            # If there is output (i.e., the button was clicked)
            if output:
                # If it's a tower select button, update the selected tower
                if isinstance(button, TowerSelectButton):
                    self.unselect_tower()
                    self.selected_tower = output
                    self.selected_button = button
                    self.selected_button.is_selected = True
                # If it's a wave start button, set wave_start to True
                elif isinstance(button, WaveStartButton):
                    self.wave_start = True
                # If it's a menu button, return the output (likely to navigate to a menu)
                elif isinstance(button, MenuButton):
                    return output
                        
    def render(self, screen):
        # Render all the buttons onto the screen
        for button in self.buttons:
            button.render(screen)

    def reset(self):
        # Reset the selected tower and wave_start flag
        self.unselect_tower()
        self.wave_start = False
