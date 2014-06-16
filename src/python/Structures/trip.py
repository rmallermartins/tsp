class Trip:
    def __init__(self, G):
        self.G = G
        self.weight = 0
        self.trip = []
    
    def addVertex(self, vertex):
        if self.trip:
            last = self.trip[len(self.trip)-1]
            self.weight += self.G.m[last-1][vertex.n-1]
        self.trip.append(vertex.n)
    
    def printTrip(self):
        print self.weight
        for v in self.trip:
            print v
