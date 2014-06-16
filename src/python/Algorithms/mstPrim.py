from sys import maxint

class MstPrim:
    def __init__(self, G, r):
        self.G = G
        self.r = r
        self.Q = []
        
    def execute(self):
        self.r.key = 0
        for v in self.G.V:
            self.Q.append(v)
            
        while self.Q:
            u = self.extractMin()
            for v in self.Q:
                if self.G.m[u.n-1][v.n-1] < v.key:
                    v.pi = u
                    v.key = self.G.m[u.n-1][v.n-1]

    def extractMin(self):
        Min = maxint
        for v in self.Q:
            if v.key < Min:
                vMin = v
                Min = v.key
        self.Q.remove(vMin)
        return vMin
