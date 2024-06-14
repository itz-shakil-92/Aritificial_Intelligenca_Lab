from queue import PriorityQueue 

# Number of vertices in the graph
v = 14

# Create a graph with v vertices
graph = [[] for i in range(v)]

def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue() 
    pq.put((0, actual_Src)) 
    visited[actual_Src] = True 

    while not pq.empty():
        u = pq.get()[1]
        print(u, end=" ") 
        if u == target:
            break
        
        for v, c in graph[u]: 
            if not visited[v]:
                visited[v] = True 
                pq.put((c, v))
    print()

def addedge(x, y, cost): 
    graph[x].append((y, cost))
    graph[y].append((x, cost))

# Add edges to the graph
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

# Define the source and target nodes
source = 0
target = 9 

# Perform Best First Search
best_first_search(source, target, v)
