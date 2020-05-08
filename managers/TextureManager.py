import pygame
from Constants import *


class TextureManager():

    def __init__(self):
        self.__images_map = dict()

    def load(self, id, name):
        new_image = pygame.image.load(name).convert()
        self.__images_map[id] = new_image

    def draw(self, id, x, y, width, height, screen):
        rect_src = pygame.Rect(x * TILESIZE, y * TILESIZE, width, height)
        screen.blit(self.__images_map[id], rect_src)
