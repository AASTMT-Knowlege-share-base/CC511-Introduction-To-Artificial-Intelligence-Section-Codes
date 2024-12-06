import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    # Priority queue for exploring nodes
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    visited = set()
    path = []
    
    while priority_queue:
        # Get the node with the smallest heuristic
        _, current = heapq.heappop(priority_queue)
        path.append(current)
        
        # If we reached the goal, return the path
        if current == goal:
            return path
        
        visited.add(current)
        
        # Explore neighbors
        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
    
    return None  # No path found

# Define the graph and heuristic
graph = {
    "A": [("B", 1), ("C", 4), ("D", 2)],
    "B": [("E", 2)],
    "C": [("F", 5)],
    "D": [("G", 1)],
    "E": [],
    "F": [],
    "G": []
}

heuristic = {
    "A": 10,
    "B": 6,
    "C": 4,
    "D": 8,
    "E": 3,
    "F": 0,
    "G": 0
}

'''

Graph:
       A(10)
     /   |   \
  B(6)  C(4)  D(8)
   |     |     |
  E(3)  F(0)  G(0) [Goal]

Costs:
A -> B (1), A -> C (4), A -> D (2)
B -> E (2), C -> F (5), D -> G (1)

'''

# Perform the search
start = "A"
goal = "G"  # The optimal goal node
path = greedy_best_first_search(graph, heuristic, start, goal)

if path:
    print("Path found by GBFS:", " -> ".join(path))
else:
    print("No path found.")

