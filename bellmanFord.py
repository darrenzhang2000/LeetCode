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

Update: It would've been much better to implement by using two for loops and going through the list of verticies and 
edges than to create a class.

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
        
        # assuming edges don't have duplicates
        for edge, cost in edges:
            current, neighbor = edge
            neighborVertice = self.graph[neighbor]
            self.graph[current].neighbors.append((neighborVertice, cost))

        self.applyBellmanFord(source, len(verticies))

    def applyBellmanFord(self, source, numVerticies):
        if source not in self.graph:
            raise Exception("Source not in graph")
        
        sourceVertice = self.graph[source]
        sourceVertice.cost = 0

        # perform v - 1 relaxations
        for _ in range(numVerticies):
            self.performRelaxations()

        # detect negative cycle

    def performRelaxations(self):
        for key in self.graph.keys():
            vertice = self.graph[key]

            if vertice.cost == float('inf'):
                continue
            
            for neighbor, cost in vertice.neighbors:
                # print("---- upating ----", "key", key, "neighbor", neighbor.name, "prev cost", neighbor.cost, "new comp", vertice.cost + cost)
                neighbor.cost = min(neighbor.cost, vertice.cost + cost)

    def containsNegativeCycle(self):
        for key in self.graph.keys():
            vertice = self.graph[key]

            if vertice.cost == float('inf'):
                continue
            
            for neighbor, cost in vertice.neighbors:
                if vertice.cost + cost < neighbor.cost:
                    return True

        return False


    def printGraph(self):
        for vertice in self.graph.keys():
            print("Vertice: ", vertice)
            for neighbor, cost in self.graph[vertice].neighbors:
                print("Neighbor", neighbor.name, "cost", neighbor.cost)
            print("\n")

    def printCosts(self):
        for key in self.graph:
            vertice = self.graph[key]
            print(vertice.name, vertice.cost)

v = [1, 2, 3, 4, 5, 6, 7]
e = [[(1, 2), 6], [(1, 3), 5], [(1, 4), 5], [(2, 5), -1], [(3, 2), -2], [(3, 5), 1], [(4, 3), -2], 
[(4, 6), -1], [(5, 7), -3], [(6, 7), 3]]
e2 = [[(1, 2), 4], [(1, 4), 5], [(2, 4), 5], [(3, 2), -10], [(4, 3), 3]]

g = Graph(v, e2, 1)
g.printCosts()
print(g.containsNegativeCycle())

