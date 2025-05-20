import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi**2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)
    for _ in range(iterations):
        neighbor = [
            min(max(current[i] + random.uniform(-0.1, 0.1), bounds[i][0]), bounds[i][1])
            for i in range(dim)
        ]
        neighbor_value = func(neighbor)
        if neighbor_value < current_value:
            if abs(current_value - neighbor_value) < epsilon:
                break
            current, current_value = neighbor, neighbor_value
        else:
            if all(abs(current[i] - neighbor[i]) < epsilon for i in range(dim)):
                break
    return current, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best)
    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)
        if candidate_value < best_value:
            if abs(best_value - candidate_value) < epsilon:
                break
            best, best_value = candidate, candidate_value
    return best, best_value


# Simulated Annealing
def simulated_annealing(
    func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    dim = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)
    best, best_value = current[:], current_value
    t = temp
    for _ in range(iterations):
        neighbor = [
            min(max(current[i] + random.uniform(-0.1, 0.1), bounds[i][0]), bounds[i][1])
            for i in range(dim)
        ]
        neighbor_value = func(neighbor)
        delta = neighbor_value - current_value
        if delta < 0 or random.random() < math.exp(-delta / t):
            current, current_value = neighbor, neighbor_value
            if current_value < best_value:
                best, best_value = current[:], current_value
        t *= cooling_rate
        if t < epsilon:
            break
        if abs(current_value - best_value) < epsilon:
            break
    return best, best_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
