import pygame
from Constants import *
from Scenes.MapScene import MapScene
from entities.Cursor import Cursor
from managers.Camera import Camera
from managers.EventManager import EventManager, EventType
from managers.TextureManager import TextureManager


class WindowManager:

    def __init__(self):
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__event_manager = EventManager()
        self.__cursor = Cursor()
        self.__scene = MapScene()
        self.__camera = Camera(self.__scene.map_manager.map.width * TILESIZE, self.__scene.map_manager.map.height * TILESIZE)
        self.clock = pygame.time.Clock()
        self.is_running = True

    def update(self):
        self.__process_event(self.__event_manager.get_event())
        self.__cursor.update(self.__scene.matrix)

    def draw(self):
        self.__screen.fill(BLACK)
        map_surface = self.__scene.draw()
        self.__screen.blit(map_surface, self.__camera.apply_map(map_surface.get_rect()))
        self.__cursor.draw(self.__screen)
        pygame.display.flip()
        self.clock.tick(60)

    def __draw_grid(self):
        for x in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(self.__screen, LIGHTGREY, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(self.__screen, LIGHTGREY, (0, y), (SCREEN_WIDTH, y))

    def __process_event(self, event):
        if event is not None:
            if event.type == EventType.Type.CURSOR:
                self.__cursor.click(event.pos)
            if event.type == EventType.Type.KEYBOARD:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def events(self):
        pass

    def quit(self):
        self.is_running = False


