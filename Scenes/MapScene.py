import numpy
from pytmx import pytmx

from Constants import *
from Scenes.BaseScene import BaseScene
from managers.TiledMapManager import TiledMapManager


class MapScene(BaseScene):

    def __init__(self):
        super().__init__()
        self.map_manager = TiledMapManager('map1/map1.tmx')
        self.map = self.map_manager.get_map()
        width = int(self.map.width)
        height = int(self.map.height)
        self.matrix = numpy.zeros((height, width))
        self.set_obstacles(self.matrix)

    def draw(self):
        surface = self.map_manager.get_surface()
        for index, layer in enumerate(self.map.visible_layers):
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.map.get_tile_image(x, y, index)
                    if tile:
                        surface.blit(tile, (x * self.map.tilewidth, y * self.map.tileheight))
        return surface

    def set_obstacles(self, matrix):
        layer = self.map.get_layer_by_name("obstacles")
        for wall in layer:
            if wall.name == "wall":
                initial = int(wall.x / TILESIZE), int(wall.y / TILESIZE)
                width = int(wall.width / TILESIZE)
                height = int(wall.height / TILESIZE)
                if width <= 0: width = 1
                if height <= 1: height = 1
                matrix[initial[1]][initial[0]] = 1
                for i in range(0, width):
                    for j in range(0, height):
                        matrix[initial[1]+j][initial[0]+i] = 1
