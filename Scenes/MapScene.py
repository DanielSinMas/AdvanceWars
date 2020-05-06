import numpy
from pytmx import pytmx

from Constants import *
from Scenes.BaseScene import BaseScene
from managers.TiledMapManager import TiledMapManager


class MapScene(BaseScene):
    def __init__(self):
        self.map_manager = TiledMapManager('map2/map2.tmx')
        self.map = self.map_manager.get_map()
        width = int(self.map.width)
        height = int(self.map.height)
        self.matrix = numpy.zeros((width, height))
        self.set_obstacles(self.matrix)
        print(self.matrix)

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
        layer = self.map.get_layer_by_name("walls")
        for wall in layer:
            initial = int(wall.x / TILESIZE), int(wall.y / TILESIZE)
            width = int(wall.width / TILESIZE)-1
            height = int(wall.height / TILESIZE)-1
            matrix[initial[1]][initial[0]] = 1
            for i in range(0, width):
                for j in range(1, height):
                    matrix[initial[1]+j][initial[0]+i] = 1
