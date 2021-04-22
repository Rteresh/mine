import pygame


class Settings:
    def __init__(self):
        self.dt = pygame.time.Clock()
        """Инициализирует настройки шахты"""
        # Screen settings
        self.screen_name = 'Mine 5-start'
        self.screen_width = 1250
        self.screen_height = 400
        self.bg_color = (255, 255, 255)
        self.start_end = 1
        self.fps = 60

        # Настройка автоматического режима
        # PSQ1
        self.start_end_PSQ1 = 1
        self.status_PSQ1 = False  # True ON False OFF
        self.done_PSQ1 = False  # True NO WORK False DONE
        self.num_comb_to_crep_to_start_PSQ1 = 14  # До какой секции должен доехать, чтобы включить PSQ1
        # PSQ2
        self.pos_turn_PSQ2 = True  # True если комбайн еще не переступил черту
        self.status_PSQ2 = False  # True ON False OFF
        self.done_PSQ2 = False  # True NO WORK False DONE
        self.num_comb_to_crep_to_start_PSQ2 = 18  # До какой секции должен доехать,чтобы включить PSQ2
        self.amount_crep_PSQ2 = 7
        self.start_end_PSQ2 = 11  # Начало с какой секции должно пойти
        self.end_PSQ2 = self.start_end_PSQ2 - self.amount_crep_PSQ2
        # PSQ3
        self.status_PSQ3 = False
        self.done_PSQ3 = False  # True NO WORK False DONE
        self.start_end_PSQ3 = 1
        self.num_comb_to_crep_to_start_PSQ3 = 13
        self.distance_between_crep_comb_PSQ = 5
        # DA1
        self.done_DA1 = False
        self.status_DA1 = False
        self.start_end_DA1 = 0
        self.distance_between_crep_comb_DA1 = 6
        self.amount_conveer_DA1 = 12

        # DA2
        self.snake_size = 6 # RAZNICA MEGDU SEKCIYAMI KOCAYA
        self.status_DA2 = False
        self.done_DA2 = False
        self.start_end_DA2 = self.amount_conveer_DA1
        self.distance_between_crep_comb_DA2 = 20
        self.amount_conveer_DA2 = 3
        self.end_DA2 = self.amount_conveer_DA1 + self.amount_conveer_DA2
        # DA3
        self.status_DA3 = False
        self.start_end_DA3 = None
        # DA_new_snake
        self.status_DAS = False
        self.start_end_DAS = self.end_DA2
        self.amount_conveer_DAS = 3 # Дополнительно сколько секций
        # Настройки комбайна
        self.combine_speed = 0.3
        self.combine_position = int(0)  # Esli дошел до последней точки = start, до первой = 0

        # Настройки секции
        self.crep_speed = 0.1

        # Настройка конвейера
        self.conveer_speed = 0.3
        self.range_cylinder = 30
        self.conveer_speed_snake_size = 0.05

    def default(self):
        self.start_end_PSQ2 = 18
        self.start_end_PSQ1 = 1






















