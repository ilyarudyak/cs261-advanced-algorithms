from gen_utils import *


def read_cities(filename='../../data/csv_samples/cities1k_100.csv'):
    """
    Read cities in dictionary: id:City
    That's different from Norvig representation as set of cities.
    """
    df = pd.read_csv(filename)
    return {city_id: City(x, y) for city_id, x, y in zip(df.CityId, df.X, df.Y)}


if __name__ == '__main__':
    cities = read_cities()
    print(cities)

