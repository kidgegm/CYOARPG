import pygame
import json
import time

def screen():
    pygame.display.set_caption('CYOARPG')  # Set the window title
    info = pygame.display.Info()
    width, height = info.current_w, info.current_h  # Get screen width and height
    return pygame.display.set_mode((width, height), pygame.NOFRAME) # Run game in borderless window mode

def font():
    filepath = '../resources/fonts/JoganSoftRegular.ttf'
    size = 64
    return pygame.font.Font(filepath, size)

def load_dialog(filepath, section):
    with open (filepath, 'r') as file:
        contents = json.load(file)
        return contents.get(section, [])