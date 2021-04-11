class Settings:
    def __init__(self):
        """Инициализирует настройки шахты"""
        # Screen settings
        self.screen_name = 'Mine 5-1'
        self.screen_width = 1250
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.distance_between_crep_comb = 6
        self.start_end = 1

        # Настройка автоматического режима

        self.start_PSQ_1 = 0  # 1 start 0 off
        self.num_crep_to_start_end_PSQ = 18
        self.comb_to_start_PSQ = 17
        self.crep_to_check_position = 9

        # Настройки комбайна
        self.combine_speed = 0.3

        self.combine_position = int(0)
        # Esli дошел до последней точки = 1, до первой = 0

        # Настройки секции
        self.crep_speed = 0.9

        self.comb_did_cleanup = 0
