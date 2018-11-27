import matplotlib.pyplot as plt
import random
import time
import itertools
import urllib
import csv
import functools
from statistics import mean, stdev

from tsp_utils import *


def alltours(cities):
    return itertools.permutations(cities)


def alltours_tsp(cities):
    """Generate all possible tours of the cities
    and choose the shortest tour."""
    return shortest_tour(alltours(cities))


def shortest_tour(tours):
    """Choose the tour with the minimum tour length."""
    return min(tours, key=tour_length)


if __name__ == '__main__':
    print(tour_length(alltours_tsp(Cities(8))))
