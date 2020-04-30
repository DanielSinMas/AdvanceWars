from pytmx import pytmx

from Scenes.BaseScene import BaseScene
from managers.TiledMapManager import TiledMapManager


class MapScene(BaseScene):
    def __init__(self):
        self.map_manager = TiledMapManager('map1/map1.tmx')
        self.map = self.map_manager.get_map()

    def draw(self):
        surface = self.map_manager.get_surface()
        for index, layer in enumerate(self.map.visible_layers):
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.map.get_tile_image(x, y, index)
                    if tile:
                        surface.blit(tile, (x * self.map.tilewidth, y * self.map.tileheight))

        return surface
