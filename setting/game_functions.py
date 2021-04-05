import sys
import pygame
from mine_objects.crep import Crep
from mine_objects.conveer import Conveer


def check_events(combine, screen, mine_settings, crep, conveer):
    """Обновление событий, которые происходят в основном классе"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            moving_combine(event, combine, screen, mine_settings)
        elif event.type == pygame.KEYUP:
            moving_combine_keyup(event, combine)


def update_screen(combine, screen, mine_settings, crep, conveer):
    combine.blitme()


def moving_combine(event, combine, screen, mine_settings):
    if event.key == pygame.K_RIGHT:
        combine.moving_right = True
    if event.key == pygame.K_LEFT:
        combine.moving_left = True


def moving_combine_keyup(event, combine):
    if event.key == pygame.K_RIGHT:
        combine.moving_right = False
    if event.key == pygame.K_LEFT:
        combine.moving_left = False


def create_crep(settings, screen, crep, crep_number, row_number, creps):
    crep = Crep(screen, settings)
    crep.x = crep.x.width
    creps.append(crep)
