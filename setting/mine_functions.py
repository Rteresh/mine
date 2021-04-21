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
    combine_update_y(combine, conveers)


def check_all_param(event, settings, screen, combine, creps, conveers):
    if event.key == pygame.K_e:
        print(f'центр комбайна{combine.rect.centerx}')
        print(f'позиция комбайна{settings.combine_position}')
        print(f'направление комбайна:{combine.direction}')
        print(f'достиг ВШ2:{combine.check_point}')
        print(f'conveer.rect.centery:{conveers[1].rect.centery}')
        print(f'crep.rect.centry{creps[1].rect.top}')
        print(f'new_position_cylinder_DA{new_position_cylinder_DA(settings, conveers[1].rect.centery)}')


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
    check_status_automatic(settings, combine)
    start_PSQ1(settings, creps, conveers)
    start_PSQ2(settings, creps, conveers)
    start_PSQ3(settings, creps, conveers)
    start_DA1(settings, creps, conveers)


def start_PSQ1(settings, creps, conveers):
    """Запуск передвижки секции на конецевых участках"""
    if settings.status_PSQ1 and settings.done_PSQ2:
        i = -settings.start_end_PSQ1
        end_PSQ1 = (len(creps)) - settings.num_comb_to_crep_to_start_PSQ1
        if creps[i].rect.top > conveers[i].rect.centery:
            creps[i].update_y()
        else:
            print(f'i = {i}')
            settings.start_end_PSQ1 += 1
        if end_PSQ1 == settings.start_end_PSQ1:
            settings.done_PSQ1 = True
            settings.status_PSQ1 = False
            settings.default()


def start_PSQ2(settings, creps, conveers):
    """Запуск передвижки секций определенно заданой в группе """
    if settings.status_PSQ2 and not settings.done_PSQ2:
        i = settings.start_end_PSQ2
        if creps[i].rect.top > conveers[i].rect.centery:
            creps[i].update_y()
        else:
            print(f'iPSQ2 =  {i}')
            if i == - 20:
                print(f'end_PSQ2 = {settings.end_PSQ2}')
                print(f'start_end_PSQ2 = {settings.start_end_PSQ2}')
            settings.start_end_PSQ2 -= 1
            if settings.end_PSQ2 == settings.start_end_PSQ2:
                print('Я ДОЛЖЕН СРАБОТАТЬ')
                settings.done_PSQ2 = True
                settings.status_PSQ2 = False
                settings.default()


def start_PSQ3(settings, creps, conveers):
    """Запуск передвижки секции относительно комбайна"""
    if settings.status_PSQ3 and settings.done_PSQ2:
        i = settings.combine_position - settings.distance_between_crep_comb_PSQ
        if creps[i].rect.top > conveers[i].rect.centery:
            creps[i].update_y()
        if i < 0:
            print('меньше нуля')
            settings.status_PSQ3 = False
            settings.done_PSQ3 = True


def start_DA1(settings, creps, conveers):
    """Запуск передвижки конвейера, не включая концевых операций"""
    if settings.status_DA1 and settings.done_PSQ3:
        i = settings.combine_position - settings.distance_between_crep_comb_DA1
        if conveers[i].rect.centery > conveers[i].nc:
            print(conveers[i].new_position_conv)
            conveers[i].update_y()
            if i == 15:
                settings.status_DA1 = False
                settings.done_PSQ2 = False
                settings.pos_turn_PSQ2 = True
        else:
            conveers[i].update_new_pos()


def start_DA2(settings, creps, conveers):
    """Запуск передвижки конвейера, установка косого заезда"""
    pass


def start_DA3(settings, creps, conveers):
    """Запуск передвжики конвейера,концевые операции"""
    pass


def check_status_automatic(settings, combine):
    if settings.combine_position == settings.num_comb_to_crep_to_start_PSQ1:
        if combine.check_point == 1 and combine.direction == 0:
            settings.status_PSQ1 = True
    elif settings.combine_position == settings.num_comb_to_crep_to_start_PSQ2 and settings.pos_turn_PSQ2:
        if combine.check_point == 1 and combine.direction == 0:
            settings.status_PSQ2 = True
            print("Я включил PSQ2")
            settings.pos_turn_PSQ2 = False

    elif settings.combine_position == settings.num_comb_to_crep_to_start_PSQ3:
        if combine.check_point == 1 and combine.direction == 0:
            settings.status_PSQ3 = True
    if settings.combine_position == settings.distance_between_crep_comb_DA1:
        if combine.check_point == 0 and combine.direction == 1:
            settings.status_DA1 = True


def combine_update_y(combine, conveers):
    for conveer in conveers:
        if combine.rect.collidepoint(conveer.rect.x, conveer.rect.y):
            combine.update_y(conveer.rect.y - combine.rect.height)


def new_position_cylinder_DA(settings, old_position):
    new_position_cylinder = old_position - settings.range_cylinder
    return new_position_cylinder
