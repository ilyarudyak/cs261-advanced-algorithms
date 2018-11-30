import numpy as np
import pandas as pd

# so we have cities 0...197768
MAX_CITY_INDEX = 197768


def tour_length(tour, cities, primes):
    """
    Compute tour length for the given tour using Euclidean distance,
    except every 10th step. If previous city index is not prime number
    we increase distance by 10%.
    :param tour: numpy array [0, 123, ..., 567] (not ending with 0)
    :param cities: dictionary with city index as key and tuple of coordinates as a value
    :param primes: dictionary number:True or False
    :return: length of the tour
    """
    return 0


def get_primes():
    df_primes = pd.read_csv('data/primes.txt')
    primes = df_primes.prime
    primes_dict = {}
    for i in range(MAX_CITY_INDEX+1):
        if i in primes.values:
            primes_dict[i] = True
        else:
            primes_dict[i] = False
    return primes_dict


if __name__ == '__main__':
    primes = get_primes()
    print(type(primes), len(primes), primes[:5], primes[-5:])
