import sys

import pygame

from settings import Settings

def run_game():
    #Game initial - create window
    pygame.init() # Create the view
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #Main loop
    while True:

        #Waiting for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Refreshing the screen in each loop's iteration
        screen.fill(ai_settings.bg_color)

        #Show the last modified view
        pygame.display.flip()

run_game()