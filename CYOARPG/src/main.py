import pygame
import util
from menu import Menu

pygame.init()

def main():
    screen = util.screen()
    font = util.font()
    background_color = (0, 0, 0)  # Set your background color

    menu = Menu(screen)
    menu.run()

    pygame.quit()

if __name__ == "__main__":
    main()