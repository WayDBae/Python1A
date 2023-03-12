import pygame, sys

def events(gun):
    """обработка событий"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                #кнопка вправо
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    gun.mright = True
                #кнопка вправо
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    gun.mright = False
                #кнопка влево
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    gun.mleft = True
                #кнопка влево
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    gun.mleft = False