def uniform_cost_search(goal, start, graph, cost):
    answer = [float('inf')] * len(goal)
    queue = [(0, start)]
    visited = set()

    while queue:
        queue.sort(reverse=True)
        cost_to_current, current_node = queue.pop()

        if current_node in goal:
            index = goal.index(current_node)
            if answer[index] == float('inf'):
                answer[index] = cost_to_current
            if all(c != float('inf') for c in answer):
                return answer

        if current_node not in visited:
            visited.add(current_node)
            for neighbor, edge_cost in graph[current_node]:
                total_cost = cost_to_current + cost[(current_node, neighbor)]
                queue.append((total_cost, neighbor))

    return answer

graph = {
    0: [(1, 2), (3, 5)],
    1: [(6, 1)],
    2: [(1, 4)],
    3: [(1, 5), (4, 2), (6, 6)],
    4: [(2, 4), (5, 3)],
    5: [(2, 6), (6, 3)],
    6: [(4, 7)]
}

cost = {
    (0, 1): 2,
    (0, 3): 5,
    (1, 6): 1,
    (3, 1): 5,
    (3, 4): 2,
    (3, 6): 6,
    (4, 2): 4,
    (4, 5): 3,
    (5, 2): 6,
    (5, 6): 3,
    (6, 4): 7
}

goal = [6]

answer = uniform_cost_search(goal, 0, graph, cost)
print("Minimum cost from 0 to 6 is =", answer[0])
