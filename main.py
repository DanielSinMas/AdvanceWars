from Game import Game

game = Game()
game.run()
from managers.algoritms.Pathfinding import Pathfinding

map = [[0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 0],
       [0, 0, 1, 1, 1, 0],
       [0, 0, 1, 0, 1, 0],
       [0, 0, 0, 0, 1, 0]]

path = Pathfinding((3, 4), (5, 5), map)
path.getPath()
