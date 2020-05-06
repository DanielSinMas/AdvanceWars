import operator
import numpy

from managers.algoritms.Node import Node


class Pathfinding:

    def __init__(self, init, destiny, map):
        self.init = init
        self.destiny = destiny
        self.map = map
        self.open = list()
        self.closed = list()
        heuristic = self.get_heuristic(self.init)
        self.open.append(Node(init[0], init[1], 0, heuristic, None))

    def getPath(self) -> str:
        while True:
            aux = list()
            for item in self.open:
                aux.append(item)
            for item in self.open:
                actual = self.check_destiny(item)
                if actual is None:
                    self.add_neighbours(item, aux)
                else:
                    path = []
                    while actual.parent is not None:
                        path.append(actual)
                        actual = actual.parent
                    path.append(actual)
                    path.reverse()

                    for item in path:
                        self.map[item.y][item.x] = "x"
                    print(numpy.matrix(self.map))
                    return ""

            self.open.clear()
            for item in sorted(aux, key=operator.attrgetter("f")):
                self.open.append(item)

    def check_destiny(self, item) -> Node:
        if (item.x, item.y) == self.destiny:
            return item
        else:
            return None

    def add_neighbours(self, item, aux):
        actual = item
        neighbours = {Node(actual.x, actual.y - 1, actual.g + 1, self.get_heuristic((actual.x, actual.y - 1)), actual),
                      Node(actual.x + 1, actual.y, actual.g + 1, self.get_heuristic((actual.x + 1, actual.y)), actual),
                      Node(actual.x, actual.y + 1, actual.g + 1, self.get_heuristic((actual.x, actual.y + 1)), actual),
                      Node(actual.x - 1, actual.y, actual.g + 1, self.get_heuristic((actual.x - 1, actual.y)), actual)}

        #Comprobar porque estos nodos no cuentan como que ya están en closed

        for node in neighbours:
            if node.x >= 0 and node.y >= 0 and node.x < len(self.map[0]) and node.y < len(self.map) and \
                    self.map[node.y][node.x] == 0 and not self.in_closed(node) and not node in self.open:
                aux.append(node)
            elif node.x >= 0 and node.y >= 0 and node.x < len(self.map[0]) and node.y < len(self.map):
                self.closed.append(node)
        aux.remove(item)
        self.closed.append(actual)

    def get_heuristic(self, origen) -> int:
        return abs(self.destiny[1] - origen[1]) + abs(self.destiny[0] - origen[0])

    def in_closed(self, node):
        for item in self.closed:
            if node.x == item.x and node.y == item.y:
                return True
        return False
