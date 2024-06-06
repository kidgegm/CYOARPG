import pygame
import settings
import time

pygame.init()

def typer(surface, font, text, position, color='#008B8B', typing_speed=30, line_delay=1):
    x, y = position  # Break down position tuple into two variables to store the location text will be displayed
    clock = pygame.time.Clock()
    for line in text:
        for char in line:
            for event in pygame.event.get():  # Event handling loop
                if event.type == pygame.QUIT:  # Check for quit event
                    pygame.quit()
                    return True  # Exit function and signal to quit the main loop
            char_surface = font.render(char, True, color)  # Renders the character to a surface
            surface.blit(char_surface, (x, y))  # Draws what was rendered to the position
            pygame.display.flip()  # Updates the display to show changes
            x += char_surface.get_width()  # Move the x coordinate to the right once a character has been typed
            time.sleep(typing_speed / 1000)  # Delay each character being typed, convert milliseconds to seconds
        y += font.get_height()  # Move the y position downwards once a line has been typed
        x = position[0]  # Reset x position for the next line of text
        time.sleep(line_delay)  # Delay between lines
    return False

def main():
    screen = settings.screen()
    font = settings.font()
    background_color = (0, 0, 0)  # Set your background color

    # Load dialogue from JSON file
    dialogue = settings.load_dialog('../resources/scripts/intro.json', 'intro')

    # Define initial position
    position = (100, 100)

    # Main loop
    running = True
    for line in dialogue:
        if typer(screen, font, [line], position):  # Pass a list containing a single line
            running = False
            break
        position = (position[0], position[1] + font.get_height())  # Update y position for next line

    pygame.quit()

if __name__ == "__main__":
    main()