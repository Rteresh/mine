import sys
import pygame
from mine_objects.crep import Crep
from mine_objects.conveer import Conveer

start_end = 1


def check_events(combine, screen, mine_settings, crep, conveer, creps, conveers):
    """Обновление событий, которые происходят в основном классе"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            moving_combine(event, combine, screen, mine_settings)
            check_all_param(event, mine_settings, screen, combine, creps, conveers)
            restart(event, conveers, creps)
        elif event.type == pygame.KEYUP:
            moving_combine_keyup(event, combine)
    # check_position_combine(mine_settings, creps, combine)


def update_screen(combine, screen, mine_settings, crep, conveer, creps, conveers):
    combine.blitme()
    combine.new_check_point()
    for one_conveer in conveers:
        one_conveer.blitme()
    for one_crep in creps:
        one_crep.blitme()
    start_automatic(mine_settings, combine, creps, conveers)


def check_all_param(event, settings, screen, combine, creps, conveers):
    if event.key == pygame.K_e:
        print(f'центр комбайна{combine.rect.centerx}')
        print(f'позиция комбайна{settings.combine_position}')
        print(f'направление комбайна:{combine.direction}')
        print(f'достиг ВШ2:{combine.check_point}')
        print(f'rect conveer:{conveers[1].rect.centery}')


def restart(event, conveers, creps):
    if event.key == pygame.K_r:
        for crep in creps:
            crep.rect.y = 735
            crep.text_image_rect.y = 767


def moving_combine(event, combine, screen, mine_settings):
    if event.key == pygame.K_RIGHT:
        combine.moving_right = True
    if event.key == pygame.K_LEFT:
        combine.moving_left = True
    if event.key == pygame.K_q:
        sys.exit()


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
        if combine.rect.centerx == creps[i].rect.x:
            settings.combine_position = creps[i].number


def start_automatic(settings, combine, creps, conveers):
    if settings.combine_position == settings.num_comb_to_crep_to_start_PSQ1:
        start_any_PSQ(combine, settings.status_PSQ1)
    elif settings.combine_position == settings.num_comb_to_crep_to_start_PSQ2:
        if combine.check_point == 1 and combine.direction == 0:
            settings.status_PSQ2 = True
    elif settings.combine_position == settings.num_comb_to_crep_to_start_PSQ3:
        if combine.check_point == 1 and combine.direction == 0:
            pass
    start_PSQ1(settings, creps, conveers)
    start_PSQ2(settings, creps, conveers)


def start_PSQ1(settings, creps, conveers):
    if settings.status_PSQ1 and settings.done_PSQ1:
        i = -settings.start_end_PSQ1
        end_PSQ1 = (len(creps)) - settings.num_comb_to_crep_to_start_PSQ1
        if creps[i].rect.top > conveers[i].rect.centery:
            creps[i].update_y()
        else:
            settings.start_end_PSQ1 += 1
        if end_PSQ1 == settings.start_end_PSQ1:
            settings.done_PSQ1 = False
            settings.status_PSQ1 = False
            settings.end_PSQ1 = 1


def start_PSQ2(settings, creps, conveers):
    if settings.status_PSQ2 and settings.done_PSQ2:
        i = settings.start_end_PSQ2
        if creps[i].rect.top > conveers[i].rect.centery:
            creps[i].update_y()
        else:
            settings.start_end_PSQ2 -= 1
            if settings.end_PSQ2 == settings.start_end_PSQ2:
                settings.done_PSQ2 = False
                settings.status_PSQ2 = False
                settings.end_PSQ2 = 1


def start_PSQ3(settings, combine, creps, conveers):
    pass


def start_any_PSQ(combine, status_PSQ):
    if combine.direction == 0 and combine.check_point == 1:
        status_PSQ = True
