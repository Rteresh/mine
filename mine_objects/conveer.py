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
        self.rect.y = crep.rect.y - 32


        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.new_position_conv = self.rect.centery - self.conveer_settins.range_cylinder
        self.nc = float(self.new_position_conv)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_y(self):
        self.y -= self.conveer_settins.conveer_speed
        self.rect.y = self.y

    def update_snake(self):
        self.y -= self.conveer_settins.conveer_speed_snake_size
        self.rect.y = self.y


    def update_new_pos(self):
        self.new_position_conv = self.rect.centery - self.conveer_settins.range_cylinder
        self.nc = self.new_position_conv
