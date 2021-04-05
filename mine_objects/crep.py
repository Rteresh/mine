import pygame


class Crep:
    """Класс для создания и управления крепи"""

    def __init__(self, mine_screen, mine_settings):
        """Инициализация крепи секции"""
        self.screen = mine_screen
        self.screen_rect = mine_screen.get_rect()
        self.crep_settings = mine_settings

        self.image = pygame.image.load('templates/crep.jpg')
        self.rect = self.image.get_rect()

        # Каждый новая секция крепи появляется в левом верхнем углу экрана.
        self.rect.x = self.screen_rect.x # Появление в краю экрана
        self.rect.y = self.screen_rect.bottom-self.rect.height
        # self.rect.rect
        # Сохранение точной позиции пришельцев
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        pass

