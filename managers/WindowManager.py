import pygame
from Constants import *
from Scenes.MapScene import MapScene
from managers.EventManager import EventManager, EventType


class WindowManager:

    def __init__(self):
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__event_manager = EventManager()
        self.__scene = MapScene(self.__screen)
        self.clock = pygame.time.Clock()
        self.is_running = True

    def update(self):
        self.__scene.process_event(self.__event_manager.get_event())
        self.__scene.update()

    def draw(self):
        self.__scene.draw()

        pygame.display.flip()
        self.clock.tick(60)

    def __draw_grid(self):
        for x in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(self.__screen, LIGHTGREY, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(self.__screen, LIGHTGREY, (0, y), (SCREEN_WIDTH, y))

    def events(self):
        pass

    def quit(self):
        self.is_running = False


