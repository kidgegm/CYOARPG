import pygame
import util

class Button:
    def __init__(self, normal_image, hover_image, pressed_image, position, callback, size=(150, 50)):
        self.normal_image = pygame.transform.scale(pygame.image.load(normal_image), size)
        self.hover_image = pygame.transform.scale(pygame.image.load(hover_image), size)
        self.pressed_image = pygame.transform.scale(pygame.image.load(pressed_image), size)
        self.image = self.normal_image
        self.rect = self.image.get_rect(topleft=position)
        self.callback = callback
        self.pressed = False
    
    def draw(self, surface):
        if self.pressed:
            self.image = self.pressed_image
        elif self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.hover_image
        else:
            self.image = self.normal_image
        surface.blit(self.image, self.rect.topleft)
    
    def check_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    self.pressed = False
                    self.callback()

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = (50, 50, 50)  # Background color for the menu

        # Define button images and positions
        self.buttons = [
            Button('resources/sprites/menu/TEST.png', 'resources/sprites/menu/TEST.png', 'resources/sprites/menu/TEST.png', (300, 200), self.start_game),
            Button('resources/sprites/menu/TEST.png', 'resources/sprites/menu/TEST.png', 'resources/sprites/menu/TEST.png', (300, 300), self.saves),
            Button('resources/sprites/menu/TEST.png', 'resources/sprites/menu/TEST.png', 'resources/sprites/menu/TEST.png', (300, 400), self.options),
            Button('resources/sprites/menu/TEST.png', 'resources/sprites/menu/TEST.png', 'resources/sprites/menu/TEST.png', (300, 500), self.exit_game)
        ]
    
    def start_game(self):
        print("Start Game")

    def saves(self):
        print("Saves Menu")

    def options(self):
        print("Options Menu")

    def exit_game(self):
        pygame.quit()
        quit()

    def run(self):
        running = True
        while running:
            self.screen.fill(self.background_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Draw and check button clicks
            for button in self.buttons:
                button.draw(self.screen)
                button.check_click()
            
            pygame.display.flip()
            pygame.time.Clock().tick(60)

        pygame.quit()