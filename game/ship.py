import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        # Initial ship
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading the image of ship
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Each new ship appear on the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Ship's middle point -float value
        self.center = float(self.rect.centerx)

        # Setting look up to ship's movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Refreshing the position of the ship acc. to the movement
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        # Refreshing rect object acc. to the self.center value
        self.rect.centerx = self.center

    def blitme(self):
        # Display ship in actual position
        self.screen.blit(self.image, self.rect)
