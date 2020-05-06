class Node:

    def __init__(self, x, y, g, h, parent):
        self.parent = parent
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g + h
