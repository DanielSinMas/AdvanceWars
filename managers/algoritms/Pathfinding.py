import datetime
import operator

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

    def getPath(self):
        before = datetime.datetime.now()
        while True:
            aux = list()
            for item in self.open:
                aux.append(item)
            if len(self.open) > 0:
                item = self.open[0]
                actual = self.check_destiny(item)
                if actual is None:
                    self.add_neighbours(item, aux)
                else:
                    path = []
                    while actual.parent is not None:
                        path.append((actual.x, actual.y))
                        actual = actual.parent
                    path.append((actual.x, actual.y))
                    path.reverse()
                    after = datetime.datetime.now()
                    difference = (after - before).total_seconds()
                    print(str(difference))
                    return path

            self.open.clear()
            for item in sorted(aux, key=operator.attrgetter("f")):
                self.open.append(item)
            self.open = sorted(self.open, key=operator.attrgetter("f"))

    def check_destiny(self, item) -> Node:
        if item.x == self.destiny[0] and item.y == self.destiny[1]:
            return item
        else:
            return None

    def add_neighbours(self, item, aux):
        actual = item
        neighbours = {
            Node(actual.x, actual.y - 1, actual.g + 1, self.get_heuristic((actual.x, actual.y - 1)), actual),
            Node(actual.x + 1, actual.y, actual.g + 1, self.get_heuristic((actual.x + 1, actual.y)), actual),
            Node(actual.x, actual.y + 1, actual.g + 1, self.get_heuristic((actual.x, actual.y + 1)), actual),
            Node(actual.x - 1, actual.y, actual.g + 1, self.get_heuristic((actual.x - 1, actual.y)), actual)}

        for node in neighbours:
            if node.x >= 0 and node.y >= 0 and node.x < len(self.map[0]) and node.y < len(self.map) and \
                    self.map[node.y][node.x] == 0 and not self.in_closed(node) and not self.in_open(node):
                if not self.in_aux(node, aux):
                    aux.append(node)
            elif node.x >= 0 and node.y >= 0 and node.x < len(self.map[0]) and node.y < len(self.map):
                self.closed.append(node)
        aux.remove(actual)
        self.closed.append(actual)

    def get_heuristic(self, origen) -> int:
        return abs(self.destiny[1] - origen[1]) + abs(self.destiny[0] - origen[0])

    def in_closed(self, node) -> bool:
        for item in self.closed:
            if item.x == node.x and item.y == node.y:
                return True
        return False

    def in_open(self, node) -> bool:
        for item in self.open:
            if item.x == node.x and item.y == node.y:
                return True
        return False

    def in_aux(self, node, aux) -> bool:
        for item in aux:
            if item.x == node.x and item.y == node.y:
                return True
        return False
