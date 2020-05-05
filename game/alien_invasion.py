import sys

import pygame

def run_game():
    # Game initial - create window
    pygame.init() # Create the view
    screen = pygame.display.set_mode((800, 600)) # Responsible for screen resolution
    pygame.display.set_caption("Alien Invasion")

    #Background color definition
    bg_color = (230, 230, 0) #Tuple with RGB setting

    # Main loop
    while True:

        #Waiting for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Refreshing the screen in each loop's iteration
        screen.fill(bg_color)

        #Show the last modified view
        pygame.display.flip()

run_game()