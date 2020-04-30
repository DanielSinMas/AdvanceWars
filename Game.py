import pygame

from managers.WindowManager import WindowManager


class Game:

    def __init__(self):
        pygame.init()
        self.window_manager = WindowManager()

    def run(self):
        while True:
            self.window_manager.update()
            self.window_manager.draw()
