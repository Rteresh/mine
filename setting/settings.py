class Settings:
    def __init__(self):
        """Инициализирует настройки шахты"""
        # Screen settings
        self.screen_name = 'Mine 5-1'
        self.screen_width = 1250
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.start_end = 1

        # Настройка автоматического режима
        # PSQ1
        self.start_end_PSQ1 = 1
        self.status_PSQ1 = False  # True ON False OFF
        self.done_PSQ1 = False  # True NO WORK False DONE
        self.num_comb_to_crep_to_start_PSQ1 = 16  # До какой секции должен доехать, чтобы включить PSQ1
        # PSQ2
        self.pos_turn_PSQ2 = True # True если комбайн еще не переступил черту
        self.status_PSQ2 = False  # True ON False OFF
        self.done_PSQ2 = False  # True NO WORK False DONE
        self.num_comb_to_crep_to_start_PSQ2 = 20  # До какой секции должен доехать,чтобы включить PSQ2
        self.amount_crep_PSQ2 = 10
        self.start_end_PSQ2 = 18  # Начало с какой секции должно пойти
        self.end_PSQ2 = self.start_end_PSQ2 - self.amount_crep_PSQ2
        # PSQ3
        self.status_PSQ3 = False
        self.done_PSQ3 = False  # True NO WORK False DONE
        self.start_end_PSQ3 = 1
        self.num_comb_to_crep_to_start_PSQ3 = 13
        self.distance_between_crep_comb_PSQ = 5
        # DA1
        self.status_DA1 = False
        self.start_end_DA1 = 0
        self.distance_between_crep_comb_DA1 = 6
        self.amount_conveer_DA1 = 16

        # DA2
        self.status_DA2 = False
        # DA3
        self.status_DA3 = False
        # Настройки комбайна
        self.combine_speed = 0.3
        self.combine_position = int(0)  # Esli дошел до последней точки = 1, до первой = 0

        # Настройки секции
        self.crep_speed = 0.5

        # Настройка конвейера
        self.conveer_speed = 0.5

    def default(self):
        self.start_end_PSQ2 = 18
        self.start_end_PSQ1 = 1