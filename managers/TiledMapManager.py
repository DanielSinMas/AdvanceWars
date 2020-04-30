from pathlib import Path

import pygame
from pytmx import load_pygame, pytmx

MAPS = 'assets/maps'


class TiledMapManager:

    def __init__(self, map_name):
        self.path_to_maps = Path(MAPS)
        map_path = self.path_to_maps / map_name
        self.map = load_pygame(map_path)
        self.width = self.map.width * self.map.tilewidth
        self.height = self.map.height * self.map.tileheight
        self.__surface = pygame.Surface((self.width, self.height))

    def get_surface(self) -> pygame.Surface:
        return self.__surface

    def get_map(self) -> pytmx.TiledMap :
        return self.map
