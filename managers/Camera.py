import pygame

from Constants import *


class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.camera = pygame.Rect(0, 0, self.width, self.height)

    def update(self, map_rect):
        pass

    def apply_map(self, map_rect):
        mouse_position = pygame.mouse.get_pos()
        position_x = self.camera.topleft[0]
        position_y = self.camera.topleft[1]
        if mouse_position[0] >= SCREEN_WIDTH - (TILESIZE * 2):
            position_x -= TILESIZE
        if mouse_position[0] <= (TILESIZE * 2):
            position_x += TILESIZE
        if mouse_position[1] >= SCREEN_HEIGHT - (TILESIZE * 2):
            position_y -= TILESIZE
        if mouse_position[1] <= (TILESIZE * 2):
            position_y += TILESIZE

        position_x = max(-(self.width - SCREEN_WIDTH), position_x)
        position_x = min(0, position_x)

        position_y = max(-(self.height - SCREEN_HEIGHT), position_y)
        position_y = min(0, position_y)

        self.camera = pygame.Rect(position_x, position_y, self.width, self.height)

        return map_rect.move(position_x, position_y)

    def apply_camera(self, unit_rect):
        return unit_rect.move(self.camera.x, self.camera.y)
