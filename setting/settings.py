class Settings:
    def __init__(self):
        """Инициализирует настройки шахты"""
        # Screen settings
        self.screen_name = 'Mine 5-1'
        self.screen_width = 1250
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.distance_between_crep_comb = 6

        # Настройки комбайна
        self.combine_speed = 0.1
        # 0 = left 1 = right
        self.combine_direction = 1
        self.combine_position = int(0)

        # Настройки секции
        self.crep_speed = 0.1