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


def nn_tsp(cities):
    """Start the tour at the first city; at each step extend the tour
    by moving from the previous city to the nearest neighboring city, C,
    that has not yet been visited."""
    start = first(cities)
    tour = [start]
    unvisited = set(cities - {start})
    while unvisited:
        C = nearest_neighbor(tour[-1], unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour


if __name__ == '__main__':
    plot_tsp(nn_tsp, Cities(10))
    plt.show()
