import enum

import pygame
from Constants import *


class EventType:

    class Type(enum.Enum):
        CURSOR = 1

    def __init__(self, type):
        self.type = type
        self.pos = (0, 0)


class EventManager:

    def __init__(self):
        pass

    def get_event(self) -> EventType:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    event = EventType(EventType.Type.CURSOR)
                    position = [0, 0]
                    position[0] = int(pos[0] / TILESIZE)
                    position[1] = int(pos[1] / TILESIZE)
                    event.pos = position
                    print(str(int(pos[0]/TILESIZE)) + " - " + str(int(pos[1]/TILESIZE)))
                    return event
