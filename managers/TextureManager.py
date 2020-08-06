import pygame
from Constants import *


class TextureManager():

    def __init__(self):
        self.__images_map = dict()

    def load(self, id, name):
        new_image = pygame.image.load(name).convert_alpha()
        self.__images_map[id] = new_image

    def draw(self, id, x, y, width, height, screen, camera):
        rect_src = pygame.Rect(x * TILESIZE, y * TILESIZE, width, height)
        image = pygame.transform.scale(self.__images_map[id], (width, height))
        screen.blit(image, camera.apply_camera(rect_src))
