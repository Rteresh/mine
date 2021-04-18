import pygame


class Conveer:
    """Класс для создания ковейера"""

    def __init__(self, mine_screen, mine_settings, crep):
        self.screen = mine_screen
        self.screen_rect = mine_screen.get_rect()
        self.conveer_settins = mine_settings

        self.image = pygame.image.load('templates/conveer.jpg')
        self.rect = self.image.get_rect()

        self.rect.x = crep.rect.x
        self.rect.y = crep.rect.y - self.rect.height

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_y(self):
        self.y -= self.
