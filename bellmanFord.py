'''
The idea behind bellman ford is that find the shortest cost in a graph to get to a certain node. 
It's particularly useful when detecting negative cycles, that is when edges sum to a negative number.

The algorithm:
Do for v - 1 times:
    for each edge:
        for each neighbor of that edge:
            compute the best cost of getting to that neighboring node, 
            which is the min(currentNeighboringValue, currentValue + cost from this node to neighbor)

Do this algorithm one more time and see if there are any updates on the vth relaxation. If so, then
there is a negative cycle.

Nodes: N(1), N(2), N(3), N(4), N(5), N(6), N(7)
Edges: (1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (4, 3), (4, 6), (5, 7), (6, 7)

Let's represent this using a graph data structure.
The graph keeps track of the min cost to get from a source node to a destination node.

For this particular implementation, I chose to implement the neighbors for each vertice as an array,
which has O(n) time when searching for a particular vertice but is more space efficient than a 2d array.
In addition, I won't be removing edges much so I decided not to go with a LinkedList.
'''

class Vertice:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.neighbors = []

class Graph:
    def __init__(self, verticies, edges, source):
        # key = name of node
        # value = {cost, neighbors}
        self.graph = {} 

        # initialize graph
        for vertice in verticies:
            if vertice not in self.graph:
                self.graph[vertice] = Vertice(vertice, float('inf'))
        
        if source not in self.graph:
            raise Exception("Source not in graph")

        # assuming edges don't have duplicates
        for current, neighbor in edges:
            neighborVertice = self.graph[neighbor]
            self.graph[current].neighbors.append(neighborVertice)
    def printGraph(self):
        for vertice in self.graph.keys():
            print("Vertice: ", vertice)
            for neighbor in self.graph[vertice].neighbors:
                print("Neighbor", neighbor.name)
            print("\n")

v = [1, 2, 3, 4, 5, 6, 7]
e = [(1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (4, 3), (4, 6), (5, 7), (6, 7)]
g = Graph(v, e, 1)
g.printGraph()

