import sys
from sys import maxint
sys.path.append("../Structures/")
from trip import Trip

class TspNn:
    def __init__(self, G):
        self.G = G
        self.r = self.G.V[0]
        self.trip = Trip(G)
        self.V = self.G.V
    
    def execute(self):
        self.trip.addVertex(self.r)
        self.V.remove(self.r)
        v = self.r
        
        while self.V:
            u = self.nearest(v)
            self.trip.addVertex(u)
            self.V.remove(u)
            v = u
        
        self.trip.addVertex(self.r)
    
    def nearest(self, u):
        Min = maxint
        for v in self.G.V:
            if self.G.m[u.n-1][v.n-1] < Min:
                nearest = v
                Min = self.G.m[u.n-1][v.n-1]
        return nearest
