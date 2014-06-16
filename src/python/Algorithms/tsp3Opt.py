import sys
sys.path.append("../Structures/")
from trip import Trip

class Tsp3Opt:
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
            variation = [0, 0, 0, 0]
            
            for a in range(n-5):
                b = a + 1
                
                for c in range(a+2, n-3):
                    d = c + 1
                    
                    if a != 0:
                        lim = n
                    else:
                        lim = n-1
                    
                    for e in range(c+2, lim):
                        
                        if e != n:
                            f = e+1
                        else:
                            f = 0
                        
                        oldWeight = self.w[self.t.trip[a]-1][self.t.trip[b]-1] \
                                    + self.w[self.t.trip[c]-1][self.t.trip[d]-1] \
                                    + self.w[self.t.trip[e]-1][self.t.trip[f]-1]
                        
                        newWeight1 = self.w[self.t.trip[a]-1][self.t.trip[e]-1] \
                                     + self.w[self.t.trip[d]-1][self.t.trip[b]-1] \
                                     + self.w[self.t.trip[c]-1][self.t.trip[f]-1]
                        
                        newWeight2 = self.w[self.t.trip[a]-1][self.t.trip[d]-1] \
                                     + self.w[self.t.trip[e]-1][self.t.trip[b]-1] \
                                     + self.w[self.t.trip[c]-1][self.t.trip[f]-1] \
                        
                        newWeight3 = self.w[self.t.trip[a]-1][self.t.trip[d]-1] \
                                     + self.w[self.t.trip[e]-1][self.t.trip[c]-1] \
                                     + self.w[self.t.trip[b]-1][self.t.trip[f]-1] \
                        
                        newWeight4 = self.w[self.t.trip[a]-1][self.t.trip[c]-1] \
                                     + self.w[self.t.trip[b]-1][self.t.trip[e]-1] \
                                     + self.w[self.t.trip[d]-1][self.t.trip[f]-1] \
                        
                        variation[0] = oldWeight - newWeight1
                        variation[1] = oldWeight - newWeight2
                        variation[2] = oldWeight - newWeight3
                        variation[3] = oldWeight - newWeight4
                        
                        for i in range(4):
                            var = variation[i]
                            if var > maxVariation:
                                maxVariation = var
                                best = (a, b, c, d, e, f)
                                nVariation = i
            
            if maxVariation != 0:
                a, b, c, d, e, f = best
                if nVariation == 0:
                    self.swap1(a, b, c, d, e, f)
                elif nVariation == 1:
                    self.swap2(a, b, c, d, e, f)
                elif nVariation == 2:
                    self.swap3(a, b, c, d, e, f)
                elif nVariation == 3:
                    self.swap4(a, b, c, d, e, f)
            else:
                self.calculateNewTrip()
                break

    def swap1(self, a, b, c, d, e, f):
        aux = self.t.trip[b]
        self.t.trip[b] = self.t.trip[e]
        self.t.trip[e] = self.t.trip[c]
        self.t.trip[c] = self.t.trip[d]
        self.t.trip[d] = aux
    def swap2(self, a, b, c, d, e, f):
        aux = self.t.trip[b]
        self.t.trip[b] = self.t.trip[d]
        self.t.trip[d] = aux
        aux = self.t.trip[e]
        self.t.trip[e] = self.t.trip[c]
        self.t.trip[c] = aux
    def swap3(self, a, b, c, d, e, f):
        aux = self.t.trip[b]
        self.t.trip[b] = self.t.trip[d]
        self.t.trip[d] = self.t.trip[c]
        self.t.trip[c] = self.t.trip[e]
        self.t.trip[e] = aux
    def swap4(self, a, b, c, d, e, f):
        aux = self.t.trip[b]
        self.t.trip[b] = self.t.trip[c]
        self.t.trip[c] = aux
        aux = self.t.trip[e]
        self.t.trip[e] = self.t.trip[d]
        self.t.trip[d] = aux
    
    def calculateNewTrip(self):
        for v in self.t.trip:
            self.nt.addVertex(self.G.V[v-1])
