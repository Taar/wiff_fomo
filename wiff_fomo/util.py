from dateutil.parser import parse
from collections import namedtuple


TimeRange = namedtuple('TimeRange', 'start end')


def parse_date_time(date, time):

    date_time = date + ' ' + time
    return parse(date_time)


def check_time_collision(reference_film, test_film):

    r = TimeRange(reference_film['start_time'], reference_film['end_time'])
    t = TimeRange(test_film['start_time'], test_film['end_time'])
    # check to see if the start time of the reference film is within the range
    # of the test film. Also check if the end time of the reference film is
    # within the test time range
    return (
        (r.start <= t.start and r.end >= t.start)
        or
        (t.start <= r.start and t.end >= r.start)
    )
