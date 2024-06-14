class Node:
    def __init__(self, state, heuristic, parent=None):
        self.state = state
        self.heuristic = heuristic
        self.parent = parent

    def __lt__(self, other):
        return self.heuristic < other.heuristic

def insert_into_priority_queue(priority_queue, node):
    if not priority_queue:
        priority_queue.append(node)
    else:
        for i, n in enumerate(priority_queue):
            if node < n:
                priority_queue.insert(i, node)
                break
        else:
            priority_queue.append(node)

def pop_from_priority_queue(priority_queue):
    return priority_queue.pop(0)

def greedy_best_first_search(start_state, goal_state, graph, heuristic):
    visited = set()
    priority_queue = []
    insert_into_priority_queue(priority_queue, Node(start_state, heuristic[start_state]))

    while priority_queue:
        node = pop_from_priority_queue(priority_queue)
        current_state = node.state

        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state == goal_state:
            path = []
            while node:
                path.append(node.state)
                node = node.parent
            return path[::-1]

        for neighbor in graph[current_state]:
            if neighbor not in visited:
                insert_into_priority_queue(priority_queue, Node(neighbor, heuristic[neighbor], node))

    return None

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B'},
    'F': {'C'}
}

heuristic = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 7,
    'E': 4,
    'F': 1
}

start = 'A'
goal = 'F'

path = greedy_best_first_search(start, goal, graph, heuristic)

if path:
    print(f"Path from {start} to {goal}: {path}")
else:
    print(f"No path found from {start} to {goal}")
