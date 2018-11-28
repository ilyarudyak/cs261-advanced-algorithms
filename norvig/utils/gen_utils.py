import matplotlib.pyplot as plt
import random
import time
import itertools
import urllib
import csv
import functools
from statistics import mean, stdev


def distance(A, B):
    """The distance between two points."""
    return abs(A - B)


def tour_length(tour):
    """The total of distances between each pair of
    consecutive cities in the tour."""
    return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))


def shortest_tour(tours):
    """Choose the tour with the minimum tour length."""
    return min(tours, key=tour_length)


class Point(complex):
    x = property(lambda self: self.real)
    y = property(lambda self: self.imag)


City = Point
Tour = list  # Tours are implemented as lists of cities


def Cities(n, width=900, height=600, seed=42):
    """Make a set of n cities, each with random coordinates
    within a (width x height) rectangle."""
    random.seed(seed * n)
    return frozenset(City(random.randrange(width), random.randrange(height))
                     for _ in range(n))


def first(collection):
    """Start iterating over collection, and return the first element."""
    return next(iter(collection))


def Maps(num_maps, num_cities):
    """Return a tuple of maps, each consisting of the given number of cities."""
    return tuple(Cities(num_cities, seed=(m, num_cities))
                 for m in range(num_maps))


@functools.lru_cache(None)
def benchmark(func, inputs):
    """Run function on all the inputs; return pair of (average_time_taken, results)."""
    t0           = time.clock()
    results      = [func(x) for x in inputs]
    t1           = time.clock()
    average_time = (t1 - t0) / len(inputs)
    return average_time, results


def benchmarks(tsp_algorithms, maps=Maps(30, 60)):
    """Print benchmark statistics for each of the algorithms."""
    for tsp in tsp_algorithms:
        time, results = benchmark(tsp, maps)
        lengths = [tour_length(r) for r in results]
        print("{:>25} |{:7.0f} ±{:4.0f} ({:5.0f} to {:5.0f}) |{:7.3f} secs/map | {} ⨉ {}-city maps"
              .format(tsp.__name__, mean(lengths), stdev(lengths), min(lengths), max(lengths),
                      time, len(maps), len(maps[0])))


if __name__ == '__main__':
    print(Maps(2, 3))

