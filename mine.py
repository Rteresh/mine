import sys
import pygame
from setting.settings import Settings
from mine_objects.combine import Combine
from mine_objects.crep import Crep
from mine_objects.conveer import Conveer
import setting.game_functions as gf


def run_game():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption(setting.screen_name)
    crep = Crep(screen, setting)
    conveer = Conveer(screen, setting, crep)
    combine = Combine(screen, conveer, setting)
    """Запуск основного цикла игры"""
    while True:
        gf.check_events(combine, screen, setting, crep, conveer)
        screen.fill(setting.bg_color)
        gf.update_screen(combine, screen, setting, crep, conveer)
        crep.blitme()
        conveer.blitme()
        combine.update()
        # Отслеживание событий  на экране,клавиатуры и мыши
        pygame.display.flip()


run_game()
