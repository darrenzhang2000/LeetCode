class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
            '''
            Kruskal's Algorithm:
            1) Create a forest F (a set of trees), where each vertex in 
            the graph is a separate tree.
            2) Create a set S containing all the edges in the graph.
            3) While S is nonempty and F is not yet spanning (fully connected):
                3A) Remove an edge with minimum weight from S
                3B) If the removed edge connects two different trees then 
                add it to the forest F, combining two trees into a single tree.
            '''
            def find(city):
                # Recursively re-set city's parent to its parent's parent.
                # Build the bush: ideally each tree/set is of height 1.
                if parent[city] != city:
                    parent[city] = find(parent[city])
                return parent[city]

            def union(c1, c2):
                root1, root2 = find(c1), find(c2)
                if root1 == root2:
                    return False
                parent[root2] = root1  # Always join roots!
                return True

            # [1] Keep track of disjoint sets. Initially each city is its own set.
            parent = {city: city for city in range(1, N+1)}
            # [2] Sort connections so we are always picking minimum cost edge.
            connections.sort(key=lambda x: x[2])
            total = 0
            for city1, city2, cost in connections:  # [3A]
                if union(city1, city2):  # [3B]
                    total += cost
            # Check that all cities are connected.
            root = find(N)
            return total if all(root == find(city) for city in range(1, N+1)) else -1
