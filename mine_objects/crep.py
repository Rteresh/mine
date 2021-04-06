import pygame


class Crep:
    """Класс для создания и управления крепи"""

    def __init__(self, mine_screen, mine_settings, number):
        """Инициализация крепи секции"""
        self.screen = mine_screen
        self.screen_rect = mine_screen.get_rect()
        self.crep_settings = mine_settings

        self.image = pygame.image.load('templates/crep.jpg')
        self.rect = self.image.get_rect()
        self.number = number

        # Каждый новая секция крепи появляется в левом верхнем углу экрана.
        self.rect.x = self.screen_rect.x  # Появление в краю экрана
        self.rect.y = self.screen_rect.bottom - self.rect.height
        # self.rect.rect
        # Сохранение точной позиции пришельцев
        self.x = float(self.rect.x)

        # TEXT_______________________________
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 30)
        self.text_image = self.font.render(str(number), True, self.text_color, self.crep_settings.bg_color)
        self.text_image_rect = self.text_image.get_rect()

        self.text_image_rect.x = self.rect.centerx
        self.text_image_rect.y = self.rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)

    def update(self, new_rect):
        self.rect.x = new_rect
        self.text_image_rect.x = self.rect.centerx-10
