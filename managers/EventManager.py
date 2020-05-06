import enum

import pygame
from Constants import *


class EventType:

    class Type(enum.Enum):
        CURSOR = 1
        KEYBOARD = 2

    def __init__(self, type):
        self.type = type
        self.pos = (0, 0)
        self.key = None


class EventManager:

    def __init__(self):
        pass

    def get_event(self) -> EventType:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    new_event = EventType(EventType.Type.CURSOR)
                    position = [0, 0]
                    position[0] = int(pos[0] / TILESIZE)
                    position[1] = int(pos[1] / TILESIZE)
                    new_event.pos = position
                    return new_event
                
            if event.type == KEYUP:
                new_event = EventType(EventType.Type.KEYBOARD)
                new_event.key = event.key
                return new_event

