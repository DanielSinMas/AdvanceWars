from Constants import TILESIZE
from entities import UnitType


class Unit:

    def __init__(self):
        self.x = 18
        self.y = 7
        self.type = UnitType.UnitType.BASIC
        self.movement = 5
        self.image = "assets/images/tank.png"
        self.width = TILESIZE
        self.height = TILESIZE
