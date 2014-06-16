import sys
sys.path.append("../Structures/")
from trip import Trip
from mstPrim import MstPrim

class TspMst:
    def __init__(self, G):
        self.G = G
        self.r = self.G.V[0]
        self.mstPrim = MstPrim(self.G, self.r)
        self.trip = Trip(G)
        
    def execute(self):
        self.mstPrim.execute()
        self.preOrder(self.r)
        self.trip.addVertex(self.r)
    
    def preOrder(self, u):
        self.trip.addVertex(u)
        for v in self.G.V:
            if v.pi == u:
                self.preOrder(v)
