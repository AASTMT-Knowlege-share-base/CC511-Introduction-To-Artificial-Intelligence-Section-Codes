import random

def calculate_conflicts(board):
    """Calculate the number of conflicting queen pairs."""
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # Check rows, diagonals
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing(board):
    """Perform hill climbing to solve the N-Queens problem."""
    n = len(board)
    while True:
        current_conflicts = calculate_conflicts(board)
        if current_conflicts == 0:
            return board  # Solution found
        
        # Generate all neighbors
        neighbors = []
        for col in range(n):
            for row in range(n):
                if row != board[col]:
                    new_board = list(board)
                    new_board[col] = row
                    neighbors.append(new_board)
        
        # Select the neighbor with the fewest conflicts
        next_board = min(neighbors, key=calculate_conflicts)
        next_conflicts = calculate_conflicts(next_board)
        
        # Stop if no improvement
        if next_conflicts >= current_conflicts:
            return None  # Local maximum
        board = next_board

# Example usage
n = 8
initial_board = [random.randint(0, n - 1) for _ in range(n)]
solution = hill_climbing(initial_board)
if solution:
    print("Solution found:", solution)
else:
    print("Stuck at local maximum.")
