import heapq

class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # Build the adjacency matrix
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w
            
        # Shortest distances array
        distances = [float("inf") for _ in range(n)]
        current_stops = [float("inf") for _ in range(n)]
        distances[src], current_stops[src] = 0, 0
        
        # Data is (cost, stops, node)
        minHeap = [(0, 0, src)]     
        
        while minHeap:
            
            cost, stops, node = heapq.heappop(minHeap)
            
            # If destination is reached, return the cost to get here
            if node == dst:
                return cost
            
            # If there are no more steps left, continue 
            if stops == K + 1:
                continue
             
            # Examine and relax all neighboring edges if possible 
            for nei in range(n):
                if adj_matrix[node][nei] > 0:
                    dU, dV, wUV = cost, distances[nei], adj_matrix[node][nei]
                    
                    # Better cost?
                    if dU + wUV < dV:
                        distances[nei] = dU + wUV
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                    elif stops < current_stops[nei]:
                        #  Better steps?
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                        
                    current_stops[nei] = stops
            
        return -1 if distances[dst] == float("inf") else distances[dst]
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         ht = defaultdict(list)
#         allFlights = set()
#         for from_, to, price in flights:
#             ht[from_].append([to, price])
#             allFlights.add(from_)
#             allFlights.add(to)
        
#         Info = collections.namedtuple('info', ('price', 'vertex', 'stops'))
        
#         prices = defaultdict(lambda : float('inf'))
#         curStops = defaultdict(lambda : float('inf'))
#         prices[src] = 0
                             
#         h = [Info(0, src, 0)]
#         # for to, price in ht[src]:
#         #     prices[to] = min(prices[to], price + prices[src])
#         #     heappush(h, Info(price, to, 0))
        
#         while h and len(h) < len(allFlights):
#             price, vertex, stops = heappop(h)
#             print(stops)
#             if vertex == dst:
#                 return price
            
#             if stops > k + 1:
#                 continue
#             for to, price in ht[vertex]:
#                 if price + prices[vertex] < prices[to]:
#                     prices[to] = price + prices[vertex]
#                     #print(vertex, to, prices[to], price + prices[vertex])
#                     heappush(h, Info(price + prices[vertex], to, stops + 1))
#                 elif stops < curStops[to]:
#                     heapq.heappush(h, Info(price + prices[vertex]), to, stops + 1)
                    
#                 curStops[to] = stops
#         print(prices.keys(), prices.values())
#         return prices[dst] if prices[dst] != float('inf') else -1
                     
                     
                     
                     
# '''
# 4
# [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
# 0
# 3
# 1

# 0
# [0,1,1]

# 1
# [1,2,1]

# 0
# [0,2,5]

# 1
# [2,3,1]


# 0: 0
# 1: 1
# 2: 2



# '''                     
            
