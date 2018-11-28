from gen_utils import *


def nearest_neighbor(A, cities):
    """Find the city in cities that is nearest to city A."""
    return min(cities, key=lambda c: distance(c, A))
