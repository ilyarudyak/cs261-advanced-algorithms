from prime_utils import *


def ptour_2opt_solver(ptour, pcities, primes):
    for base_index in range(9, len(ptour), 10):
        probe_index = get_close_prime(ptour, primes, base_index=base_index)
        if probe_index:
            improvement = is_alt_better(ptour, pcities, base_index, probe_index)
            if improvement > 0:
                print(f'base_index:{base_index} probe_index:{probe_index} FIND IMPROVEMENT:{improvement}!')
        #     else:
        #         print(f'base_index:{base_index} probe_index:{probe_index} ...')
        # else:
        #     print(f'base_index:{base_index} no probe_index ...')


if __name__ == '__main__':
    # pcities = read_pcities(filename='../data/samples/csv_samples/cities1k_10000.csv')
    # ptour = read_ptour(filename='../data/samples/tour_samples/linkern_cities1k_10000.tour')

    pcities = read_pcities(filename='../data/cities.csv')
    ptour = read_ptour(filename='../lk_solvers/linkern/best/linkern_full_1516735.tour')

    primes = get_primes(n=len(ptour))
    ptour_2opt_solver(ptour, pcities, primes)

