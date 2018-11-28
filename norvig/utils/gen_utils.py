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
