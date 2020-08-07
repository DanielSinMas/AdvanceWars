import numpy
import pygame
from pygame.rect import Rect
from pytmx import pytmx

from Constants import *
from Scenes.BaseScene import BaseScene
from entities.Cursor import Cursor
from entities.EntityType import EntityType
from entities.Unit import Unit
from managers.Camera import Camera
from managers.EventManager import EventType
from managers.TextureManager import TextureManager
from managers.TiledMapManager import TiledMapManager


class MapScene(BaseScene, Cursor.CursorCallback):

    def __init__(self, screen):
        super().__init__()
        self.map_manager = TiledMapManager('map1/map1.tmx')
        self.map = self.map_manager.get_map()
        width = int(self.map.width)
        height = int(self.map.height)
        self.matrix = numpy.zeros((width, height))
        self.set_obstacles(self.matrix)
        self.unities = []
        self.texture_manager = TextureManager()
        self.unities.append(Unit())
        self.__camera = Camera(self.map_manager.map.width * TILESIZE,
                               self.map_manager.map.height * TILESIZE)
        self.__cursor = Cursor(self)
        self.surface = screen
        self.__map_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

        for unit in self.unities:
            self.matrix[unit.x][unit.y] = EntityType.UNIT.value
            self.texture_manager.load(unit.image, unit.image)

    def draw(self):
        map_surface = self.draw_map()
        self.surface.blit(map_surface, self.__camera.apply_map(map_surface.get_rect()))
        self.__cursor.draw(self.surface, self.__camera)
        self.draw_units()

    def draw_map(self):
        surface = self.map_manager.get_surface()
        for index, layer in enumerate(self.map.visible_layers):
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.map.get_tile_image(x, y, index)
                    if tile:
                        surface.blit(tile, (x * self.map.tilewidth, y * self.map.tileheight))
        return surface

    def draw_units(self):
        for unit in self.unities:
            self.texture_manager.draw(unit.image, unit.x, unit.y, unit.width, unit.height, self.surface, self.__camera)
        return self.surface

    def update(self):
        self.__cursor.update(self.matrix)
        pass

    def process_event(self, event):
        if event is not None:
            if event.type == EventType.Type.CURSOR:
                position_rect = self.__camera.apply_camera_cursor(Rect(event.pos[0] * TILESIZE, event.pos[1] * TILESIZE, 0, 0))
                click_position = (int(position_rect.x / TILESIZE), int(position_rect.y / TILESIZE))
                print(click_position)
                entity_selected = self.matrix[click_position[0]][click_position[1]]
                if entity_selected == EntityType.UNIT.value:
                    for unit in self.unities:
                        if unit.x == click_position[0] and unit.y == click_position[1]:
                            self.__cursor.click(unit)
                            break
                else:
                    self.__cursor.click(click_position)
            if event.type == EventType.Type.KEYBOARD:
                if event.key == pygame.K_ESCAPE:
                    pass

    def set_obstacles(self, matrix):
        layer = self.map.get_layer_by_name("obstacles")
        for wall in layer:
            if wall.name == "wall":
                initial = int(wall.x / TILESIZE), int(wall.y / TILESIZE)
                width = int(wall.width / TILESIZE)
                height = int(wall.height / TILESIZE)
                if width <= 0:
                    width = 1
                if height <= 1:
                    height = 1
                matrix[initial[0]][initial[1]] = 1
                for i in range(0, width):
                    for j in range(0, height):
                        matrix[initial[0] + i][initial[1] + j] = 1

    def move_unit(self, unit, new_pos):
        unit_pos = (unit.x, unit.y)
        for unit in self.unities:
            if unit.x == unit_pos[0] and unit.y == unit_pos[1]:
                unit.x = new_pos[0]
                unit.y = new_pos[1]
                break
        self.matrix[new_pos[0]][new_pos[1]] = EntityType.UNIT.value
