import pygame
import settings
import game
import menus
import time

pygame.init()

def typer(surface, font, text, position, color='#008B8B', delay=0.1):
    x, y = position # Break down position tuple into two variables to store the location text will be displayed
    clock = pygame.time.Clock()
    for line in text:
        for event in pygame.event.get():  # Event handling loop
            if event.type == pygame.QUIT:  # Check for quit event
                pygame.quit()
                return  # Exit function
    for char in text:
        print(x)
        char_surface = font.render(char, True, color) # Renders the character to a surface
        surface.blit(char_surface, (x, y)) # Draws what was rendered to the position
        pygame.display.flip() # Updates the display to show changes
        x += char_surface.get_width() # Move the x coordinate to the right once a character has been typed
        time.sleep(delay) # Delay each character being typed
    y += font.get_height() # Move the y position downwards once a line has been typed
    x = position[0] # Reset x position for the next line of text
    pygame.time.delay(1000) # Delay between lines

def main():
    font = settings.font()
    screen = settings.screen()
    dialog = settings.load_dialog('./resources/scripts/intro.json', 'intro')
    for line in dialog:
        typer(screen, font, line, (100, 100))

if __name__ == "__main__":
    main()