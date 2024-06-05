import pygame

def screen():
    return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def font():
    filepath = 'C:/Users/mcgib/Documents/CYOARPG/resources/fonts/JoganSoftRegular.ttf'
    size = 64
    return pygame.font.Font(filepath, size)