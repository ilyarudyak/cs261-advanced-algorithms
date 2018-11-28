from gen_utils import *


def nearest_neighbor(A, cities):
    """Find the city in cities that is nearest to city A."""
    return min(cities, key=lambda c: distance(c, A))


def sample(population, k, seed=42):
    """Return a list of k elements sampled from population.
    Set random.seed with seed."""
    if k is None or k > len(population):
        return population
    random.seed(len(population) * k * seed)
    return random.sample(population, k)



