import heapq

class MstPrim:
    def __init__(self, G):
        self.G = G
        self.r = G.V["0"]
        self.r.key = 0
        self.Q = []
        for key, v in G.V.iteritems()
            heapq.heappush(Q, (v.key, v.n, v))
        
    def execute(self):
        while self.Q:
            (key1, n1, u) = heapq.heappop(self.Q)
            for (key2, n2, v) in self.Q:
                if self.G.m[n1, n2]
