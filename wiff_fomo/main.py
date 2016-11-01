import json
import copy
import pytz
import time
from datetime import timedelta
from email import utils
from .util import parse_date_time, check_time_collision
from itertools import count


def main(path, save_path):

    with open(path, 'r') as fp:
        films = json.load(fp)

    print("Add Missing end times ...")
    films = add_missing_end_times(films)
    print("Injecting date data ...")
    films = inject_useful_data(films)
    print("Ordering by date ...")
    films = order_by_date(films)
    print("Adding collision data ...")
    films = add_collision_data(films)
    print("Replacing date objects as strings ...")
    films = make_json_serializable(films)

    with open(save_path, 'w') as fp:
        json.dump(films, fp)


def by_date(film):
    return film['start_time']


def order_by_date(films):
    return sorted(films, key=by_date)


def add_missing_end_times(films):

    for film in films:
        if not film['End Time']:
            start_time = parse_date_time(film['Date'], film['Start Time'])
            end_time = start_time + timedelta(minutes=film['Run Time'])
            film['End Time'] = end_time.strftime("%I:%M %p")
    return films


def inject_useful_data(films):

    counter = count(start=1)
    for film in films:
        film['id'] = next(counter)
        start_time = parse_date_time(film['Date'], film['Start Time'])
        end_time = parse_date_time(film['Date'], film['End Time'])
        film['start_time'] = start_time
        film['end_time'] = end_time

    return films


def add_collision_data(films):

    films_copy = copy.deepcopy(films)
    for film, _ in zip(films_copy, films):
        film['collisions'] = copy.deepcopy(find_collisions(films, film))

    return films_copy


def local_time_stamp(date):
    timezone = pytz.timezone('US/Eastern')
    tuple_ = timezone.localize(date)
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    return tuple_.strftime(fmt)


def make_json_serializable(films):
    for film in films:
        for c_film in film['collisions']:
            c_film['start_time'] = local_time_stamp(c_film['start_time'])
            c_film['end_time'] = local_time_stamp(c_film['end_time'])

        film['start_time'] = local_time_stamp(film['start_time'])
        film['end_time'] = local_time_stamp(film['end_time'])

    return films


def find_collisions(films, test_film):
    collision_films = []

    for film in films:
        if film['id'] != test_film['id']:
            if check_time_collision(test_film, film):
                collision_films.append(film)

    return collision_films
