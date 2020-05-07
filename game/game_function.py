import sys
import pygame


def check_events():
    # Reactions to clicks and keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
