import pygame

from managers.WindowManager import WindowManager


class Game:

    def __init__(self):
        pygame.init()
        self.window_manager = WindowManager()

    def run(self):
        while self.window_manager.is_running:
            self.window_manager.events()
            self.window_manager.update()
            self.window_manager.draw()

        pygame.quit()
