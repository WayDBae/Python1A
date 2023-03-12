import pygame, controls
import sys
from mygun import Gun

def run():

    pygame.init()
    screen = pygame.display.set_mode((1200,700))
    pygame.display.set_caption("Космические Защитники!")
    bg_color = (0,0,0)
    gun = Gun(screen)

    while True:
        controls.events(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()

run()