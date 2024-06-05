import pygame
import settings
import game
import menus

pygame.init()

def main():
    font = settings.font()
    screen = settings.screen()

    text = font.render('HERE YE HERE YE!', True, (255, 255, 255))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))  # Clear screen with black color
        screen.blit(text, (100, 100))  # Draw text on screen
        pygame.display.flip()  # Update the display
    pygame.quit()

if __name__ == "__main__":
    main()