import sys
import pygame
from settings import Settings

def run_game():
    pygame.init()
    al_settings=Settings()
    screen = pygame.display.set_mode(
            (al_settings.screen_width,al_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # set backgroundcolor
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(al_settings.bg_color)

        # set screen visible
        pygame.display.flip()

run_game()
