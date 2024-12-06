import heapq

def sma_star_search(graph, costs, heuristic, start, goal, memory_limit=3):
    # Priority queue to store open nodes (limited by memory)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, []))  # (f(n), g(n), node, path)
    
    while open_list:
        # Check memory usage
        if len(open_list) > memory_limit:
            # Remove the least promising node (highest f(n))
            open_list.sort(reverse=True, key=lambda x: x[0])
            open_list.pop()
        
        # Get the most promising node
        _, g_cost, current_node, path = heapq.heappop(open_list)
        path = path + [current_node]
        
        # If we reached the goal, return the path
        if current_node == goal:
            return path, g_cost
        
        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            new_g_cost = g_cost + cost
            f_cost = new_g_cost + heuristic[neighbor]
            heapq.heappush(open_list, (f_cost, new_g_cost, neighbor, path))
    
    return None, None  # No solution found

# Define the graph
graph = {
    "A": [("B", 1), ("C", 4), ("D", 2)],
    "B": [("E", 2)],
    "C": [("F", 1)],
    "D": [("G", 1)],
    "E": [],
    "F": [],
    "G": []
}

# Define heuristic values
heuristic = {
    "A": 10,
    "B": 6,
    "C": 4,
    "D": 8,
    "E": 3,
    "F": 0,
    "G": 0  # Goal node
}

'''

       A
     / | \
   B(1) C(4) D(2)
    |    |    |
   E(2)  F(1) G(1) [Goal]

'''

# Perform the search
start = "A"
goal = "G"
memory_limit = 3  # Limit the memory to 3 nodes
path, total_cost = sma_star_search(graph, graph, heuristic, start, goal, memory_limit)

if path:
    print(f"Path found by SMA*: {' -> '.join(path)} with total cost: {total_cost}")
else:
    print("No path found within memory constraints.")
