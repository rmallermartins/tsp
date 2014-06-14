import sys

def readFile(filename):
    vertexes = []
    f = open(filename)
    for line in f:
        line = line.strip()
        line = line.split(' ')
        vertex = Vertex(line[0], line[1], line[2])
        vertexes.append(vertex)
    return vertexes

def main():
    filename = argv[2]
    alg = argv[1]
    
    vertexes = readFile(filename)
    graph = Graph(vertexes)
    
    

if __name__ == "__main__":
    main()
