import heapq

def weighted_a_star_search(graph, costs, heuristic, start, goal, weight=1.5):
    # Priority queue for nodes to explore
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (f(n), node)
    
    # Store the actual cost to reach each node
    g_cost = {start: 0}
    
    # Track the path
    came_from = {}
    
    while priority_queue:
        # Get the node with the smallest f(n)
        _, current = heapq.heappop(priority_queue)
        
        # If we reach the goal, reconstruct the path
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]  # Reverse the path
        
        # Explore neighbors
        for neighbor, cost in graph[current]:
            tentative_g_cost = g_cost[current] + cost  # g(n) for the neighbor
            
            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                # Update the cost to reach the neighbor
                g_cost[neighbor] = tentative_g_cost
                # Calculate f(n) with weighting
                f_cost = tentative_g_cost + weight * heuristic[neighbor]
                heapq.heappush(priority_queue, (f_cost, neighbor))
                # Update the path
                came_from[neighbor] = current
    
    return None  # No path found

# Define the graph and costs
graph = {
    "A": [("B", 1), ("C", 4), ("D", 2)],
    "B": [("E", 2)],
    "C": [("F", 1)],
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

       A(10)
     /   |   \
  B(6)  C(4)  D(8)
   |     |     |
  E(3)  F(0)  G(0) [Goal]

Costs:
A -> B (1), A -> C (4), A -> D (2)
B -> E (2), C -> F (1), D -> G (1)

'''

# Perform the search
start = "A"
goal = "G"
weight = 1.5  # Adjust the weight as needed
path = weighted_a_star_search(graph, graph, heuristic, start, goal, weight)

if path:
    print("Path found by Weighted A*:", " -> ".join(path))
else:
    print("No path found.")
