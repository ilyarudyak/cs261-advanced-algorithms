import matplotlib.pyplot as plt
import random
import time
import itertools
import urllib
import csv
import functools
from statistics import mean, stdev

from gen_utils import *
from plot_utils import *


def alltours_tsp(cities):
    """Generate all possible tours of the cities
    and choose the shortest tour."""
    return shortest_tour(alltours(cities))


if __name__ == '__main__':
    plot_tsp(alltours_tsp, Cities(8))
    plt.show()
