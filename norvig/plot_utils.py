import matplotlib.pyplot as plt
import random
import time
import itertools
import urllib
import csv
import functools
from statistics import mean, stdev


def plot_tour(tour):
    """Plot the cities as circles and the
    tour as lines between them."""
    plot_lines(list(tour) + [tour[0]])


def plot_lines(points, style='bo-'):
    """Plot lines to connect a series of points."""
    plt.plot([p.x for p in points], [p.y for p in points], style)
    plt.axis('scaled')
    plt.axis('off')


def plot_tsp(algorithm, cities):
    """Apply a TSP algorithm to cities, plot the resulting tour,
    and print information."""
    # Find the solution and time how long it takes
    t0 = time.clock()
    tour = algorithm(cities)
    t1 = time.clock()
    assert valid_tour(tour, cities)
    plot_tour(tour)
    plt.show()
    print("{} city tour with length {:.1f} in {:.3f} secs for {}"
          .format(len(tour), tour_length(tour), t1 - t0, algorithm.__name__))


def valid_tour(tour, cities):
    """Is tour a valid tour for these cities?"""
    return set(tour) == set(cities) and len(tour) == len(cities)