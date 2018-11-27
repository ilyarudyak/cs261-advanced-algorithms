import numpy as np


def tour_length(tour):
    """
    Compute tour length for the given tour using Euclidean distance,
    except every 10th step. If previous city index is not prime number
    we increase distance by 10%.
    :param tour: numpy array [0, 123, ..., 567] (not ending with 0)
    :return: length of the tour
    """
    return 0