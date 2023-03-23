import pygame, controls
import sys
from mygun import Gun
from pygame.sprite import Group


def run():

    pygame.init()
    screen = pygame.display.set_mode((800,700))
    pygame.display.set_caption("Космические Защитники!")
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group()
    
    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, bullets)
        controls.update_bullets(bullets) 
        

run()