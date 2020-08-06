import pygame
from Constants import *
from managers.algoritms.Pathfinding import Pathfinding


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        self.groups = pygame.sprite.Group()
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.position_x = 0
        self.position_y = 0
        self.rect.x = self.position_y
        self.rect.y = self.position_y
        self.selecting_path = False
        self.initial_position = [0, 0]
        self.final_position = [0, 0]
        self.path = list()
        self.clicked = False
        self.position = None

    def set_position(self, position):
        self.position_x = int(position[0] * TILESIZE)
        self.position_y = int(position[1] * TILESIZE)
        self.rect.x = self.position_x
        self.rect.y = self.position_y

    def update(self, map_matrix):
        pos = pygame.mouse.get_pos()
        position = (int(pos[0] / TILESIZE), int(pos[1] / TILESIZE))
        if self.clicked:
            if self.position is None:
                self.position = position
            else:
                if position[0] is not self.position[0] or position[1] is not self.position[1]:
                    if abs(position[1] - self.initial_position[1]) + abs(position[0] - self.initial_position[0]) <= 8 \
                            and map_matrix[position[1]][position[0]] == 0:
                        self.path.clear()
                        self.position = position
                        result = Pathfinding(self.initial_position, self.position, map_matrix)
                        self.path = result.getPath()
        self.position_x = int(position[0] * TILESIZE)
        self.position_y = int(position[1] * TILESIZE)
        self.rect.x = self.position_x
        self.rect.y = self.position_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        image = pygame.Surface((TILESIZE, TILESIZE))
        image.fill(GREEN_CURSOR)
        rect = image.get_rect()
        if self.path is not None and self.clicked:
            for node in self.path:
                rect.x = node[0] * TILESIZE
                rect.y = node[1] * TILESIZE
                screen.blit(image, rect)

    def click(self, position):
        if self.clicked:
            self.clicked = False
            if self.path is not None:
                self.path.clear
                self.position = None

        else:
            self.initial_position[0] = position[0]
            self.initial_position[1] = position[1]
            self.clicked = True
            if self.path is not None: self.path.clear()


