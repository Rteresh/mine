import pygame


class Combine:
    """Класс для управления комбайном"""

    def __init__(self, mine_screen, conveer, settings, crep):
        """Инициализация коробля и начальной позиции"""
        self.screen = mine_screen
        self.screen_rect = mine_screen.get_rect()
        self.combine_settings = settings
        self.crep = crep

        #      Zagruzka photo combine
        # 0 = left 1 = right
        self.direction = 1
        # 0 = left 1 = right
        self.check_point = 0

        self.image = pygame.image.load('templates/combine.jpg')
        self.rect = self.image.get_rect()
        self.moving_right = False
        self.moving_left = False
        # Evry new combine set bottom
        # С левого края

        # self.rect.x = float(self.screen_rect.left + self.rect.centerx)
        self.rect.x = 700
        self.rect.y = float(conveer.rect.y - self.rect.height)

        self.centerx = float(self.rect.x)

    def blitme(self):
        """Рисует комбайн"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Обновление позиции комбана"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.combine_settings.combine_speed
            self.direction = 1
            self.check_position()
            self.rect.x = self.centerx

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.combine_settings.combine_speed
            self.direction = 0
            self.check_position()
            self.rect.x = self.centerx

    def check_position(self):
        """Определеят позицию комбайна по эндкодору"""
        self.combine_settings.combine_position = int(self.rect.centerx / self.crep.rect.width)

    def update_y(self, new_pos):
        self.rect.y = new_pos

    def new_check_point(self):
        if self.rect.x == self.screen_rect.x:
            self.check_point = 0
        elif self.rect.right == self.screen_rect.right:
            self.check_point = 1

    def rock_cleanup(self):
        """Начинает зачисчаться и старт автоматики"""
        if self.combine_settings.combine_position == self.combine_settings.comb_to_start_PSQ:
            self.combine_settings.start_PSQ_1 = 1


