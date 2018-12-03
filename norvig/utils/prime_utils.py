from gen_utils import *
import sympy


def read_cities_prime(filename='../../data/samples/csv_samples/cities1k_100.csv'):
    """
    Read cities in dictionary: id:City
    That's different from Norvig representation as set of cities.
    """
    df = pd.read_csv(filename)
    return {cid: City(x, y) for cid, x, y in zip(df.CityId, df.X, df.Y)}


def read_tour_prime(filename='../../data/samples/tour_samples/linkern_cities1k_100.tour'):
    with open(filename) as f:
        tour = f.read().split()
    return [int(cid) for cid in tour[1:]]


def tour_length_prime_no_penalty(tour_prime, cities_prime):
    """
    tour_prime is a list of cities ids, not cities itself.
    """
    tour_cities = [cities_prime[cid] for cid in tour_prime]
    return tour_length(tour_cities)


def tour_length_prime_penalty(tour_prime, cities_prime):
    primes = list(sympy.primerange(0, len(tour_prime)))
    penalty = []
    for cid in range(9, len(tour_prime), 10):
        if tour_prime[cid] not in primes:
            penalty.append((cid, .1 * distance(cities_prime[tour_prime[cid]],
                                               cities_prime[(tour_prime[(cid+1) % len(tour_prime)])])))
        else:
            penalty.append((cid, 0))
    print(penalty)
    return sum([p for _, p in penalty])


if __name__ == '__main__':
    cities_prime = read_cities_prime()
    tour_prime = read_tour_prime()
    tour_prime[19] = 83
    tour_prime[20] = 52
    print(tour_length_prime_no_penalty(tour_prime, cities_prime))
    print(tour_length_prime_penalty(tour_prime, cities_prime))
