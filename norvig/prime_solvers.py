from prime_utils import *


def ptour_2opt_solver(ptour, pcities, primes):
    for base_index in range(9, len(ptour), 10):
        probe_index = get_close_prime(ptour, primes, base_index=base_index)
        if probe_index:
            is_better = is_alt_better(ptour, pcities, base_index, probe_index)
            if is_better:
                print(f'base_index:{base_index} probe_index:{probe_index} FIND IMPROVEMENT!')
            else:
                print(f'base_index:{base_index} probe_index:{probe_index} ...')
        else:
            print(f'base_index:{base_index} no probe_index ...')


if __name__ == '__main__':
    pcities = read_pcities(filename='../data/samples/csv_samples/cities1k_100.csv')
    ptour = read_ptour(filename='../data/samples/tour_samples/linkern_cities1k_100.tour')
    primes = get_primes()
    ptour_2opt_solver(ptour, pcities, primes)

