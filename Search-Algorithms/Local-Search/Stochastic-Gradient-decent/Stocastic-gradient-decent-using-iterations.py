def gradient_descent(objective_function, gradient_function, initial_x, learning_rate, iterations):
    """Perform Gradient Descent to minimize a function."""
    x = initial_x  # Initial solution
    for i in range(iterations):
        # Evaluate the objective function (for tracking progress)
        current_value = objective_function(x)
        print(f"Iteration {i + 1}: x = {x}, f(x) = {current_value}")
        
        # Compute the gradient (derivative of the objective function)
        gradient = gradient_function(x)
        
        # Update the solution based on the gradient
        x = x - learning_rate * gradient
        
        # Optionally, check for convergence (not implemented here)
    return x

# Objective function: f(x) = x^2 + 4x + 4
def f(x):
    return x**2 + 4 * x + 4  # Objective function to minimize

# Gradient of the objective function: f'(x) = 2x + 4
def gradient(x):
    return 2 * x + 4

# Example usage
initial_x = 10  # Starting point
learning_rate = 0.1
iterations = 20

solution = gradient_descent(f, gradient, initial_x, learning_rate, iterations)
print(f"Optimal solution: x = {solution}, f(x) = {f(solution)}")
