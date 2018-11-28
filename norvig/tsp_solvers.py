from utils.gen_utils import *
from utils.plot_utils import *
from utils.nbf_utils import *
from nn_utils import *


def alltours_tsp(cities):
    """Generate all possible tours of the cities
    and choose the shortest tour."""
    return shortest_tour(alltours(cities))


def alltours_tsp_first(cities):
    """Generate all possible tours of the cities
    and choose the shortest tour."""
    return shortest_tour(alltours_first(cities))


def nn_tsp(cities, start=None):
    """Start the tour at the first city; at each step extend the tour
    by moving from the previous city to the nearest neighboring city, C,
    that has not yet been visited."""
    if start is None:
        start = first(cities)  # fix first city
    tour = [start]  # add it to the tour (now tour is list)
    unvisited = set(cities - {start})  # remove it from unvisited
    while unvisited:
        C = nearest_neighbor(tour[-1], unvisited)  # run helper function with the last city in tour
        tour.append(C)  # append the closest city to our tour
        unvisited.remove(C)  # remove it from unvisited
    return tour


def repeated_nn_tsp(cities, repetitions=100):
    """Repeat the nn_tsp algorithm starting from each city;
    return the shortest tour."""
    return shortest_tour(nn_tsp(cities, start)
                         for start in sample(cities, repetitions))


if __name__ == '__main__':
    def repeat_10_nn_tsp(cities):
        return repeated_nn_tsp(cities, 10)

    def repeat_100_nn_tsp(cities):
        return repeated_nn_tsp(cities, 100)

    plot_tsp(nn_tsp, Cities(300))
    plot_tsp(repeat_10_nn_tsp, Cities(300))
    plot_tsp(repeat_100_nn_tsp, Cities(300))
    plt.show()
