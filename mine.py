import sys
from setting.settings import Settings
from mine_objects.combine import Combine
from mine_objects.crep import Crep
from mine_objects.conveer import Conveer
import setting.mine_functions as mf
from threading import Thread
import pygame


def run_game():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption(setting.screen_name)
    crep = Crep(screen, setting, 1)
    conveer = Conveer(screen, setting, crep)
    combine = Combine(screen, conveer, setting, crep)
    conveers, creps = [], []
    mf.create_all_creps(setting, screen, crep, creps)
    mf.create_all_conveers(setting, screen, conveer, conveers, creps)
    """Запуск основного цикла игры"""
    while True:
        mf.check_events(combine, screen, setting, crep, conveer, creps, conveers)
        screen.fill(setting.bg_color)
        mf.update_screen(combine, screen, setting, crep, conveer, creps, conveers)
        combine.update()
        # Отслеживание событий  на экране,клавиатуры и мыши
        pygame.display.flip()


run_game()
