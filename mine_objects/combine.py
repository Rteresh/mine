import pygame


class Combine:
    """Класс для управления комбайном"""

    def __init__(self, mine_screen, conveer, settings):
        """Инициализация коробля и начальной позиции"""
        self.screen = mine_screen
        self.screen_rect = mine_screen.get_rect()
        self.combine_settings = settings

        #      Zagruzka photo combine

        self.image = pygame.image.load('templates/combine.jpg')
        self.rect = self.image.get_rect()
        self.moving_right = False
        self.moving_left = False
        # Evry new combine set bottom
        # С левого края

        self.rect.x = float(self.screen_rect.left + self.rect.centerx)
        self.rect.y = float(conveer.rect.y - self.rect.height)

        self.centerx = float(self.rect.x)

    def blitme(self):
        """Рисует комбайн"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Обновление позиции комбана"""
        if self.moving_right:
            self.centerx += self.combine_settings.combine_speed
        if self.moving_left:
            self.centerx -= self.combine_settings.combine_speed

        self.rect.centerx = self.centerx
