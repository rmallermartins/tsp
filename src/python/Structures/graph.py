from sys import maxint
from math import sqrt

class Graph:
    def __init__(self, vertexes):
        self.nVertexes = len(vertexes)
        self.V = []
        self.m = [[0 for j in range(self.nVertexes)] for i in range(self.nVertexes)]
        for i in range(self.nVertexes):
            for j in range(i+1, self.nVertexes):
                self.m[i][j] = self.dist(vertexes[i], vertexes[j])
                self.m[j][i] = self.m[i][j]
            self.V.append(vertexes[i])
    
    def dist(self, u, v):
        dx = u.x - v.x
        dy = u.y - v.y
        dist = int(sqrt(dx * dx + dy * dy) + 0.5)
        return dist
