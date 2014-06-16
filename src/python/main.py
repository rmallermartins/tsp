import sys
sys.path.append("Structures/")
from graph import Graph
from trip import Trip
from vertex import Vertex
sys.path.append("Algorithms/")
from tspMst import TspMst
from tspNn import TspNn
from tsp2Opt import Tsp2Opt
from tsp3Opt import Tsp3Opt

def readFile(filename):
    vertexes = []
    f = open(filename)
    for line in f:
        line = line.strip()
        line = line.split(' ')
        vertex = Vertex(int(line[0]), float(line[1]), float(line[2]))
        vertexes.append(vertex)
    return vertexes

def main():
    filename = sys.argv[2]
    alg = sys.argv[1]
    
    vertexes = readFile(filename)
    G = Graph(vertexes)
    
    if alg == "tsp-mst":
        tspMst = TspMst(G)
        tspMst.execute()
        tspMst.trip.printTrip()
    
    elif alg == "tsp-nn":
        tspNn = TspNn(G)
        tspNn.execute()
        tspNn.trip.printTrip()
    
    elif alg == "tsp-mst-2opt":
        tspMst = TspMst(G)
        tspMst.execute()
        tsp2Opt = Tsp2Opt(tspMst.trip, G)
        tsp2Opt.execute()
        tsp2Opt.nt.printTrip()
    
    elif alg == "tsp-nn-2opt":
        tspNn = TspNn(G)
        tspNn.execute()
        G = Graph(vertexes)
        tsp2Opt = Tsp2Opt(tspNn.trip, G)
        tsp2Opt.execute()
        tsp2Opt.nt.printTrip()
    
    elif alg == "tsp-nn-3opt":
        tspNn = TspNn(G)
        tspNn.execute()
        G = Graph(vertexes)
        tsp3Opt = Tsp3Opt(tspNn.trip, G)
        tsp3Opt.execute()
        tsp3Opt.nt.printTrip()
        

if __name__ == "__main__":
    main()
