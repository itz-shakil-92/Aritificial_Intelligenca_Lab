from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, maxDepth, visited):
        print(f"Visiting Node {src}, Depth: {maxDepth}")
        visited.append(src)

        if src == target:
            return True
        if maxDepth <= 0:
            return False

        for i in self.graph[src]:
            if self.DLS(i, target, maxDepth - 1, visited):
                return True
        return False

    def IDDFS(self, src, target, maxDepth):
        for depth in range(maxDepth + 1):
            print(f"Starting new iteration with depth limit: {depth}")
            visited = []
            if self.DLS(src, target, depth, visited):
                print(f"Visited nodes in this iteration: {visited}")
                return True
            print(f"Visited nodes in this iteration: {visited}")

        print(f"All depths searched. Target not found within depth {maxDepth}")
        return False


# Create a graph given in the above diagram
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

target = 6
maxDepth = 3
src = 0

if g.IDDFS(src, target, maxDepth):
    print("Target is reachable from source within max depth")
else:
    print("Target is NOT reachable from source within max depth")
