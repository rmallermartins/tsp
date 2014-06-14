class Trip:
    def __init__(self, graph):
        self.graph = graph
        self.weight = 0
        self.trip = []
    
    def addVertex(self, vertex):
        if self.trip:
            last = self.trip[len(self.trip)]
            self.weight += graph.m[last][vertex]
        self.trip.append(vertex)
