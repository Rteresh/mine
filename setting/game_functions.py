import sys
import pygame
from mine_objects.crep import Crep
from mine_objects.conveer import Conveer


def check_events(combine, screen, mine_settings, crep, conveer, creps):
    """Обновление событий, которые происходят в основном классе"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            moving_combine(event, combine, screen, mine_settings)
        elif event.type == pygame.KEYUP:
            moving_combine_keyup(event, combine)
    # check_position_combine(mine_settings, creps, combine)


def update_screen(combine, screen, mine_settings, crep, conveer, creps, conveers):
    combine.blitme()
    for one_conveer in conveers:
        one_conveer.blitme()
    for one_crep in creps:
        one_crep.blitme()
    RSQ(mine_settings, creps, conveers)
    print(f"position  {mine_settings.combine_position}")


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
        new_crep = Crep(screen, settings, i + 2)
        new_crep.update_x(creps[i].rect.x + new_crep.rect.width)
        creps.append(new_crep)


def create_all_conveers(settings, screen, first_conveer, conveers, creps):
    conveers.append(first_conveer)
    for i in range(len(creps) - 1):
        new_conveer = Conveer(screen, settings, creps[i + 1])
        conveers.append(new_conveer)


def check_position_combine(settings, creps, combine):
    """Вычисление позиции комбайна отностильно секции крепи"""
    for i in range(len(creps) - 1):
        if combine.rect.centerx == creps[i].rect.centerx:
            settings.combine_position = creps[i].number


def RSQ(settings, creps, conveers):
    num = int(settings.combine_position / settings.distance_between_crep_comb)
    print(f"сейчас должна поехать {num}")
    if creps[num - 1].rect.top > conveers[num - 1].rect.centery:
        for i in range(10):
            creps[num - 1].update_y()
