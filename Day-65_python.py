# Implement a genetic algorithm for optimizing a function.
print("\nRuban Gino Singh - Day 65 of #100DaysOfCode\n")

print("Python program to Implement a Genetic Algorithm for Optimizing a Function\n")

import numpy as np

def objective_function(x):
    return x**2 + 4*x + 4  

population_size = 50
generations = 100
mutation_rate = 0.1
crossover_rate = 0.8

def initialize_population(size):
    return np.random.uniform(low=-10, high=10, size=(size,))

def evaluate_fitness(population):
    return np.array([objective_function(x) for x in population])

def select_parents(population, fitness):
    probabilities = fitness / fitness.sum()
    selected_indices = np.random.choice(np.arange(len(population)), size=len(population), p=probabilities)
    return population[selected_indices]

def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def mutate(individual):
    mutation_point = np.random.randint(0, len(individual))
    individual[mutation_point] += np.random.uniform(-1, 1)
    return individual

def genetic_algorithm():
    population = initialize_population(population_size)

    for generation in range(generations):
        fitness = evaluate_fitness(population)

        parents = select_parents(population, fitness)

        offspring = []
        for i in range(0, len(parents), 2):
            if np.random.rand() < crossover_rate:
                child1, child2 = crossover(parents[i], parents[i + 1])
                offspring.extend([child1, child2])
            else:
                offspring.extend([parents[i], parents[i + 1]])

        for i in range(len(offspring)):
            if np.random.rand() < mutation_rate:
                offspring[i] = mutate(offspring[i])

        population = np.concatenate([parents, offspring])

        sorted_indices = np.argsort(fitness)
        population = population[sorted_indices[:population_size]]

        best_individual = population[0]
        best_fitness = objective_function(best_individual)
        print(f"Generation {generation + 1}, Best Fitness: {best_fitness}, Best Individual: {best_individual}")

    final_best_individual = population[0]
    final_best_fitness = objective_function(final_best_individual)
    print("\nFinal Result:")
    print(f"Best Fitness: {final_best_fitness}, Best Individual: {final_best_individual}")

genetic_algorithm()

# --------------------------------------------------------- #