import pygame


class Ship:
    def __init__(self, screen):
        # Initial ship
        self.screen = screen

        # Loading the image of ship
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Each new ship appear on the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Setting look up to ship's movement
        self.moving_right = False

    def update(self):
        # Refreshing the position of the ship acc. to the movement
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        # Display ship in actual position
        self.screen.blit(self.image, self.rect)
