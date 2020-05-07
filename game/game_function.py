import sys
import pygame


def check_events():
    # Reactions to clicks and keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move the ship to the right
                ship.rect.centerx += 1

def update_screen(ai_settings, screen, ship):
    # Update view on the screen and pass to another screen
    # Refreshing the screen in each loop's iteration
    screen.fill(ai_settings.bg_color)
    ship.blitme()
