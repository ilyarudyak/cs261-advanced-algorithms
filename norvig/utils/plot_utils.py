import matplotlib.pyplot as plt
import time

from gen_utils import *


# def plot_tour(tour):
#     """Plot the cities as circles and the
#     tour as lines between them."""
#     plot_lines(list(tour) + [tour[0]])


def plot_tour(tour):
    """Plot the cities as circles and the tour as lines between them.
    Start city is red square."""
    start = tour[0]
    plot_lines(list(tour) + [start])
    plot_lines([start], 'rs')  # Mark the start city with a red square


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


def plot_labeled_lines(points, *args):
    """Plot individual points, labeled with an index number.
    Then, args describe lines to draw between those points.
    An arg can be a matplotlib style, like 'ro--', which sets the style until changed,
    or it can be a list of indexes of points, like [0, 1, 2], saying what line to draw."""
    # Draw points and label them with their index number
    plot_lines(points, 'bo')
    for (label, p) in enumerate(points):
        plt.text(p.x, p.y, '  '+str(label))
    # Draw lines indicated by args
    style = 'bo-'
    for arg in args:
        if isinstance(arg, str):
            style = arg
        else: # arg is a list of indexes into points, forming a line
            Xs = [points[i].x for i in arg]
            Ys = [points[i].y for i in arg]
            plt.plot(Xs, Ys, style)
    plt.axis('scaled')
    plt.axis('off')
