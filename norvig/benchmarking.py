from gen_utils import *
from tsp_solvers import *


def repeat_10_nn_tsp(cities):
    return repeated_nn_tsp(cities, 10)


def repeat_25_nn_tsp(cities):
    return repeated_nn_tsp(cities, 25)


def repeat_50_nn_tsp(cities):
    return repeated_nn_tsp(cities, 50)


def repeat_100_nn_tsp(cities):
    return repeated_nn_tsp(cities, 100)


if __name__ == '__main__':
    algorithms = [nn_tsp, repeat_10_nn_tsp, repeat_25_nn_tsp,
                  repeat_50_nn_tsp, repeat_100_nn_tsp]
    benchmarks(algorithms, Maps(30, 60))
