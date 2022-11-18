from collections import namedtuple, deque
from copy import deepcopy
from enum import Enum

class Node:

    def __init__(self, sheepwolfLeft, side, sheepwolfRight):
        self.sheepwolfLeft = sheepwolfLeft
        self.side = side
        self.sheepwolfRight = sheepwolfRight
        self.prev = None

    def is_valid(self):
        if 0 < self.sheepwolfLeft[0] < self.sheepwolfLeft[1] or 0 < self.sheepwolfRight[0] < self.sheepwolfRight[1]:
            return False
        if self.sheepwolfLeft[0] < 0 or self.sheepwolfLeft[1] < 0 or self.sheepwolfRight[0] < 0 or self.sheepwolfRight[1] < 0:
            return False
        return True

    def __eq__(self, other):
        return (self.sheepwolfLeft[0] == other.sheepwolfLeft[0] and self.sheepwolfLeft[1] == other.sheepwolfLeft[1] and
                self.sheepwolfRight[0] == other.sheepwolfRight[0] and
                self.sheepwolfRight[1] == other.sheepwolfRight[1] and self.side == other.side)

    def __hash__(self):
        return hash((self.sheepwolfLeft[0], self.sheepwolfLeft[1], self.side, self.sheepwolfRight[0]
                     , self.sheepwolfRight[1]))

    def goal(self):
        if self.sheepwolfLeft[0] == 0 and self.sheepwolfLeft[1] == 0:
            return True
        return False


class SemanticNetsAgent:
    def __init__(self):
        pass

    def neighbors(self,Node):
        pos_moves = [(1,1),(0,2),(2,0),(0,1),(1,0)]
        valid_moves = []
        for move in pos_moves:

            newNeighbor = deepcopy(Node)
            newNeighbor.prev = Node

            newNeighbor.side = 1-Node.side
            if Node.side == 0:
                newNeighbor.sheepwolfRight[0] += move[0]
                newNeighbor.sheepwolfRight[1] += move[1]
                newNeighbor.sheepwolfLeft[0] -= move[0]
                newNeighbor.sheepwolfLeft[1] -= move[1]

            elif Node.side == 1:
                newNeighbor.sheepwolfRight[0] -= move[0]
                newNeighbor.sheepwolfRight[1] -= move[1]
                newNeighbor.sheepwolfLeft[0] += move[0]
                newNeighbor.sheepwolfLeft[1] += move[1]

            if newNeighbor.is_valid():
                valid_moves.append(newNeighbor)

        return valid_moves

    def bfs(self, start):

        seen = set()
        found = [start]

        while found:
            node = found.pop(0)

            if node.goal():
                return node

            seen.add(node)

            for neighbor in self.neighbors(node):
                if neighbor in seen:
                    continue
                if neighbor not in found:
                    found.append(neighbor)

    def solve(self, initial_sheep, initial_wolves):

        # Definig my initial state
        if(initial_sheep == 1 and initial_wolves == 1):
            return [(1,1)]

        initial_state = Node([initial_sheep, initial_wolves], 0,[0,0])

        moves = []
        solution = []
        ans = self.bfs(initial_state)
        while ans:
            solution.append(ans)
            ans = ans.prev

        temp = [0,0]
        for a in solution:
            moves.append((abs(temp[0]-a.sheepwolfRight[0]),abs(temp[1]-a.sheepwolfRight[1])))
            temp = (a.sheepwolfRight[0], a.sheepwolfRight[1])

        return moves[1:]