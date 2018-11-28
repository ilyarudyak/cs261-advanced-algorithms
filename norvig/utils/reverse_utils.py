from gen_utils import *
from plot_utils import *


def reverse_segment_if_better(tour, i, j):
    """If reversing tour[i:j] would make the tour shorter, then do it."""
    # Given tour [...A-B...C-D...], consider reversing B...C to get [...A-C...B-D...]
    A, B, C, D = tour[i-1], tour[i], tour[j-1], tour[j % len(tour)]
    # Are old edges (AB + CD) longer than new ones (AC + BD)? If so, reverse segment.
    if distance(A, B) + distance(C, D) > distance(A, C) + distance(B, D):
        tour[i:j] = reversed(tour[i:j])


def all_segments(N):
    """Return (start, end) pairs of indexes that form segments of tour of length N."""
    return [(start, start + length)
            for length in range(N, 2-1, -1)
            for start in range(N - length + 1)]


def alter_tour(tour):
    """Try to alter tour for the better by reversing segments."""
    original_length = tour_length(tour)
    for (start, end) in all_segments(len(tour)):
        reverse_segment_if_better(tour, start, end)
    # If we made an improvement, then try again; else stop and return tour.
    if tour_length(tour) < original_length:
        return alter_tour(tour)
    return tour


cross = [City(9, 3), City(3, 10), City(2, 16), City(3, 21), City(9, 28),
         City(26, 3), City(32, 10), City(33, 16), City(32, 21), City(26, 28)]

if __name__ == '__main__':
    plot_tour(alter_tour(Tour(cross)))
    plt.show()

