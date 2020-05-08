import pygame
from settings import Settings
from ship import Ship
import game_function as gf


def run_game():
    # Game initial - create window
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Creating the ship
    ship = Ship(ai_settings, screen)

    # Main loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        # Show the last modified view
        pygame.display.flip()


run_game()
