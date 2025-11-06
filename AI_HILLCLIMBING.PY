import random

# Objective function (to maximize or minimize)
def objective_function(x):
    # Example: f(x) = -x² + 6x + 2 (Maximum at x = 3)
    return -x**2 + 6*x + 2

# Hill Climbing algorithm
def hill_climbing(max_iterations=1000, step_size=0.1):
    # Initialize with a random solution (start point)
    current_solution = random.uniform(-10, 10)
    current_value = objective_function(current_solution)

    for i in range(max_iterations):
        # Generate a small random neighboring solution
        neighbor = current_solution + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor)

        # If neighbor is better, move there
        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value

        # Optional: print intermediate results
        # print(f"Iteration {i}: x = {current_solution:.4f}, f(x) = {current_value:.4f}")

    return current_solution, current_value

# Main
if __name__ == "__main__":
    best_x, best_value = hill_climbing(max_iterations=1000, step_size=0.05)
    print("Best Solution Found:")
    print(f"x = {best_x:.4f}")
    print(f"f(x) = {best_value:.4f}")
