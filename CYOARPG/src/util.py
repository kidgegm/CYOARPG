import pygame
import json
import math

def screen():
    pygame.display.set_caption('CYOARPG')  # Set the window title
    info = pygame.display.Info() # Get display info
    width, height = info.current_w, info.current_h  # Get screen width and height
    return pygame.display.set_mode((width, height), pygame.NOFRAME) # Run game in borderless window mode

def determine_font_size():
        base_font_size = 16  # Base font size for reference
        info = pygame.display.Info() # Get display info
        width, height = info.current_w, info.current_h  # Get current screen width and height
        screen_diagonal = math.sqrt(width ** 2 + height ** 2) # Get screen diagonal
        scale_factor = screen_diagonal / 1080  # Use 1080p as a reference resolution
        return int(base_font_size * scale_factor) # Return the new font size

def font():
    filepath = './resources/fonts/JoganSoftRegular.ttf'
    size = determine_font_size()
    return pygame.font.Font(filepath, size)

def load_dialog(filepath, section):
    with open (filepath, 'r') as file:
        contents = json.load(file)
        return contents.get(section, [])