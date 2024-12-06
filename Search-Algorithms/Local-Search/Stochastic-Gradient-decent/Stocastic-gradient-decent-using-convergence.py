def gradient_descent(objective_function, gradient_function, initial_x, learning_rate, tolerance, max_iterations):
    """
    Perform Gradient Descent to minimize a function.
    
    Parameters:
        objective_function: The function to minimize.
        gradient_function: The derivative of the objective function.
        initial_x: The starting value of x.
        learning_rate: Step size for updates.
        tolerance: Threshold for stopping the algorithm.
        max_iterations: Maximum number of iterations allowed.
    
    Returns:
        x: The optimal value of x.
        history: A list of (x, f(x)) values at each iteration for tracking.
    """
    x = initial_x
    history = [(x, objective_function(x))]  # Track progress
    for i in range(max_iterations):
        gradient = gradient_function(x)  # Compute the gradient
        new_x = x - learning_rate * gradient  # Update x
        
        # Log progress
        history.append((new_x, objective_function(new_x)))
        print(f"Iteration {i + 1}: x = {new_x}, f(x) = {objective_function(new_x)}, Gradient = {gradient}")
        
        # Check for convergence
        if abs(new_x - x) < tolerance:
            print("Converged.")
            break
        
        x = new_x
    
    return x, history

# Define the objective function
def f(x):
    return 2 * x**2 - 12 * x + 20

# Define the gradient of the objective function
def gradient(x):
    return 4 * x - 12

# Parameters for gradient descent
initial_x = 0  # Starting point
learning_rate = 0.1
tolerance = 1e-6
max_iterations = 1000

# Perform Gradient Descent
optimal_x, history = gradient_descent(f, gradient, initial_x, learning_rate, tolerance, max_iterations)
optimal_cost = f(optimal_x)

print(f"Optimal number of units (x): {optimal_x}")
print(f"Minimum production cost: {optimal_cost}")
