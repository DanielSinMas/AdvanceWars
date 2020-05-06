import pygame
from Constants import *


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        self.groups = pygame.sprite.Group()
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN_CURSOR)
        self.rect = self.image.get_rect()
        self.position_x = 0
        self.position_y = 0
        self.rect.x = self.position_y
        self.rect.y = self.position_y
        self.selecting_path = False
        self.initial_position = [0, 0]
        self.final_position = [0, 0]

    def set_position(self, position):
        pos = pygame.mouse.get_pos()
        self.position_x = int(pos[0] * TILESIZE)
        self.position_y = int(pos[1] * TILESIZE)
        self.rect.x = self.position_x
        self.rect.y = self.position_y

    def update(self):
        pos = pygame.mouse.get_pos()
        position = (int(pos[0] / TILESIZE), int(pos[1] / TILESIZE))
        self.position_x = int(position[0] * TILESIZE)
        self.position_y = int(position[1] * TILESIZE)
        self.rect.x = self.position_x
        self.rect.y = self.position_y

    def click(self, position):
        if self.selecting_path:
            self.final_position[0] = position[0]
            self.final_position[1] = position[1]
            self.selecting_path = False
            print("Path:")
            print("Initial: %s" %str(self.initial_position))
            print("Final: %s" % str(self.final_position))
            #Calcular path
        else:
            self.initial_position[0] = position[0]
            self.initial_position[1] = position[1]
            self.selecting_path = True


