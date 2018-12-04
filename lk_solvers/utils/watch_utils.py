from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from linkern_utils import *
import shutil
import time
from datetime import datetime


class MyHandler(FileSystemEventHandler):

    def __init__(self, score=1516800):
        self.best_score = score
        super().__init__()

    def on_modified(self, event):

        # score this tour file
        tour = read_tour(tour_file)
        cities = pd.read_csv('../data/cities.csv', index_col=['CityId'])
        score = score_tour(tour, cities)
        int_score = int(score)

        # copy tour file to best dir if it's score is bigger than BEST_SCORE
        if score < self.best_score:
            self.best_score = int_score
            tour_file_copy = f'../linkern/best/linkern_full_{int_score}.tour'
            shutil.copy2(tour_file, tour_file_copy)
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'time: {dt} current score: {int_score} BEST SCORE!', flush=True)
        else:
            print(f'time: {dt} current score: {int_score} ...', flush=True)


if __name__ == "__main__":
    tour_dir = '../linkern/tours'
    tour_file = '../linkern/tours/linkern_full.tour'

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=tour_dir, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
