from gen_utils import *


def alltours(cities):
    return itertools.permutations(cities)


def alltours_first(cities):
    """Return a list of tours, each a permutation of cities,
    but each one starting with the same city."""
    start = first(cities)
    return [[start] + Tour(rest)
            for rest in itertools.permutations(cities - {start})]


if __name__ == '__main__':
    print(alltours_first({1, 2, 3}))
