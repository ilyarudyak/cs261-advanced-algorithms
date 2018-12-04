from gen_utils import *
from plot_utils import *
import sympy


def get_primes(n=100):
    return set(sympy.primerange(0, n))


def read_pcities(filename='../../data/samples/csv_samples/cities1k_100.csv'):
    """
    Read cities in dictionary: id:City
    That's different from Norvig representation as set of cities.
    """
    df = pd.read_csv(filename)
    return {cid: City(x, y) for cid, x, y in zip(df.CityId, df.X, df.Y)}


def read_ptour(filename='../../data/samples/tour_samples/linkern_cities1k_100.tour'):
    with open(filename) as f:
        ptour = f.read().split()
    return [int(i) for i in ptour[1:]]


def ptour_length_no_penalty(ptour, pcities):
    """
    tour_prime is a list of cities ids, not cities itself.
    """
    ptour_cities = [pcities[i] for i in ptour]
    return tour_length(ptour_cities)


def ptour_length_penalty(ptour, pcities):
    primes = get_primes(len(ptour))
    penalty = []
    for cid in range(9, len(ptour), 10):
        if ptour[cid] not in primes:
            penalty.append((cid, .1 * distance(pcities[ptour[cid]],
                                               pcities[(ptour[(cid + 1) % len(ptour)])])))
        else:
            penalty.append((cid, 0))
    print(penalty)
    return sum([p for _, p in penalty])


def ptour_length(ptour, pcities):
    return ptour_length_no_penalty(ptour, pcities) + \
           ptour_length_penalty(ptour, pcities)


def plot_ptour(ptour, pcities):
    primes = get_primes(len(ptour))
    ptour_cities = [pcities[i] for i in ptour]

    nine_pos = list(range(9, len(ptour), 10))
    ptour_primes = [i for i in range(len(ptour)) if ptour[i] in primes]

    plot_labeled_lines(ptour_cities, range(-1, 100),
                       'gs', nine_pos,
                       'rx', ptour_primes)
    plt.show()


def get_close_prime(ptour, primes, base_index=0, nodes=3):
    """
    Get index of closest prime for given node within nodes distance
    from given node. In our sample of 100 cities: returns 20 for 19;
    returns None for 69.
    """
    # check if given city is not prime
    if ptour[base_index] in primes:
        return None

    for i in range(base_index+1, base_index+nodes):
        if ptour[i] in primes:
            return i

    return None


if __name__ == '__main__':
    pcities = read_pcities()
    ptour = read_ptour()
    primes = get_primes()
    plot_ptour(ptour, pcities)
