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


def update_screen(combine, screen, mine_settings, crep, conveer, creps):
    combine.blitme()
    for one_crep in creps:
        one_crep.blitme()


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


def create_all_creps(settings, screen, first_crep, creps):
    amount_creps = int((settings.screen_width - 100) / first_crep.rect.width)
    creps.append(first_crep)
    for i in range(amount_creps):
        new_crep = Crep(screen, settings, i)
        new_crep.update(creps[i - 1].rect.x + new_crep.rect.width)
        creps.append(new_crep)
        new_crep.blitme()
    print(len(creps))



