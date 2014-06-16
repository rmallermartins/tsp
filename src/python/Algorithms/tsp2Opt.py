import sys
sys.path.append("../Structures/")
from trip import Trip

class Tsp2Opt:
    def __init__(self, t, G):
        self.G = G
        self.t = t
        self.w = G.m
        self.nt = Trip(G)
    
    def execute(self):
        while True:
            n = len(self.t.trip)-1
            maxVariation = 0
            best = None
        
            for a in range(n-3):
                b = a+1
            
                if a != 0:
                    lim = n
                else:
                    lim = n-1
                
                for c in range(a+2, lim):
            
                    if c != n:
                        d = c+1
                    else:
                        d = 0
                    
                    variation = self.w[self.t.trip[a]-1][self.t.trip[b]-1] + self.w[self.t.trip[c]-1][self.t.trip[d]-1] \
                                - self.w[self.t.trip[a]-1][self.t.trip[c]-1] - self.w[self.t.trip[b]-1][self.t.trip[d]-1]
                
                    if variation > maxVariation:
                        maxVariation = variation
                        best = a, b, c, d
                    
            if maxVariation != 0:
                a, b, c, d = best
                aux = self.t.trip[b]
                self.t.trip[b] = self.t.trip[c]
                self.t.trip[c] = aux
            else:
                self.calculateNewTrip()
                break
    
    def calculateNewTrip(self):
        for v in self.t.trip:
            self.nt.addVertex(self.G.V[v-1])
