import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    # Priority queue to hold nodes to explore
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))  # (heuristic value, node)
    
    # Track visited nodes
    visited = set()
    path = []  # Path to goal
    
    while priority_queue:
        # Get the node with the smallest heuristic value
        _, current = heapq.heappop(priority_queue)
        path.append(current)
        
        # If we reached the goal, return the path
        if current == goal:
            return path
        
        # Mark the node as visited
        visited.add(current)
        
        # Explore neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
    
    # If no path is found
    return None

# Define the graph and heuristic
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E", "F"],
    "D": [],
    "E": [],
    "F": []
}

heuristic = {
    "A": 10,
    "B": 6,
    "C": 4,
    "D": 4,
    "E": 2,
    "F": 0  # Goal node
}
'''
Graph:
       A(10)
     /   \
  B(6)   C(4)
   |     / \
  D(4)  E(2) F(0) [Goal]


'''
# Perform search
start = "A"
goal = "F"
path = greedy_best_first_search(graph, heuristic, start, goal)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found.")
