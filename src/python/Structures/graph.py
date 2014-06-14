from math import sqrt

class Graph:
    def __init__(self, vertexes):
        nVertexes = len(vertexes)
        self.m = [[0 for j in range(nVertexes)] for i in range(nVertexes)]
        for i in range(nVertexes):
            for j in range(i+1, nVertexes):
                self.m[i][j] = self.dist(vertexes[i], vertexes[j])
                self.m[j][i] = self.m[i][j]
    
    def dist(self, u, v):
        dx = u.x - v.x
        sy = u.y - v.y
        dist = int(sqrt(dx * dx + dy * dy) + 0.5)
        return dist
