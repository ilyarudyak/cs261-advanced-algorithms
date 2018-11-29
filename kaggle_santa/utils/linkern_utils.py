import pandas as pd
import numpy as np
import sympy as sympy


def write_tsp(cities, filename, name='traveling-santa-2018-prime-paths'):
    with open(filename, 'w') as f:
        f.write('NAME : %s\n' % name)
        f.write('COMMENT : %s\n' % name)
        f.write('TYPE : TSP\n')
        f.write('DIMENSION : %d\n' % len(cities))
        f.write('EDGE_WEIGHT_TYPE : EUC_2D\n')
        f.write('NODE_COORD_SECTION\n')
        for row in cities.itertuples():
            f.write('%d %.11f %.11f\n' % (row.Index+1, row.X, row.Y))
        f.write('EOF\n')


def read_tour(filename):
    tour = open(filename).read().split()[1:]
    tour = list(map(int, tour))
    if tour[-1] == 0:
        tour.pop()
    return tour


def score_tour(tour):
    df = cities.reindex(tour + [0]).reset_index()
    primes = list(sympy.primerange(0, len(cities)))
    df['prime'] = df.CityId.isin(primes).astype(int)
    df['dist'] = np.hypot(df.X - df.X.shift(-1), df.Y - df.Y.shift(-1))
    df['penalty'] = df['dist'][9::10] * (1 - df['prime'][9::10]) * 0.1
    return df.dist.sum() + df.penalty.sum()


def write_submission(tour, filename):
    assert set(tour) == set(range(len(tour)))
    pd.DataFrame({'Path': list(tour) + [0]}).to_csv(filename, index=False)


if __name__ == '__main__':

    # multiply coordinates by 1000, here's the reason:
    # concorde's EUC_2D norm rounds the distances between cities
    # to the nearest integer (source) whereas competition metric doesn't;
    # this significantly hurts quality as we get closer to TSP optimum".
    cities = pd.read_csv('../data/cities.csv', index_col=['CityId'])
    # cities1k = cities * 1000
    # write_tsp(cities1k, '../data/cities1k.tsp')

    date, n = '20181129', 1
    tour = read_tour('../data/linkern.tour')
    write_submission(tour, f'../submissions/submission_{date}_{n}.csv')
    print(score_tour(tour))