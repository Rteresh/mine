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

    run_PSQ(mine_settings, combine, creps, conveers)
    # PKN(mine_settings,conveers,combine)


def check_all_param(event, settings, screen, combine, creps, conveers):
    if event.key == pygame.K_e:
        print(f'центр комбайна{combine.rect.centerx}')
        print(f'позиция комбайна{settings.combine_position}')
        print(f'{creps[0].rect.right}')
        print(f'конвейер коор{creps[1].rect.y}')
        print(f'номер{creps[1].text_image_rect.y}')


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


def RSQ(settings, creps, conveers, combine):
    # последняя секция едет, потому что
    num = int(settings.combine_position - settings.distance_between_crep_comb)
    if combine.check_point == 1 and combine.direction == 0:
        if settings.combine_position >= settings.distance_between_crep_comb + 1:
            if creps[num - 1].rect.top > conveers[num - 1].rect.centery:
                creps[num - 1].update_y()


def PKN(settings, conveers, combine):
    for conveer in conveers:
        if conveer.rect.x + conveer.rect.width == combine.rect.x:
            print(f'секция ню{conveer.rect.y}')
            combine.update_y(conveer.rect.top - combine.rect.height)
            print(f"высокая точка коневейера {conveer.rect.top}")


def no_PSQ(settings, combine, creps, conveers, start_end=1):
    i = -settings.start_end
    if creps[i].rect.top > conveers[i].rect.centery:
        creps[i].update_y()
        if creps[i].rect.top == conveers[i].rect.centery:
            settings.start_end += 1
        if settings.start_end > 7:
            settings.start_end = 1


def run_PSQ(settings, combine, creps, conveers):
    if combine.direction == 0 and combine.check_point == 1:
        if settings.combine_position <= settings.num_crep_to_start_end_PSQ:
            no_PSQ(settings, combine, creps, conveers)
        RSQ(settings, creps, conveers, combine)


def new_PSQ(settings, combine, creps, conveers):
    i = settings.comb_to_start_PSQ - 1
    if settings.combine_position:
        if combine.direction == 1 and combine.check_point == 1:
            if creps[i].rect.top == conveers[i].rect.centery:
                if i > settings.crep_to_check_position:
                    creps[i].update_y()
                    settings.comb_to_start_PSQ -= 1


def start_automaticks(settings,screen,combine,creps,conveers):
    """Запуск автоматики"""
    if settings.combine_position == settings.comb_to_start_PSQ:
        start_comb_cleanup(settings,combine)


def start_comb_cleanup(settings,combine):
    """Комбайн начинает зачищать породу и запуск группы секций"""
    if settings.comb_did_cleanup == 0:
        if combine.direction == 1 and combine.check_point == 1:
            settings.start_PSQ_1 = 1
            settings.comb_did_cleanup = 1

    if settings.start_PSQ_1:
        pass

