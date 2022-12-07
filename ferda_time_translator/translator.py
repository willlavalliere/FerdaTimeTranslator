import sys
from bisect import bisect_right
from datetime import datetime

from .constants import ferda_time


def low_bound_bisect(a, x):
    i = bisect_right(a, x)
    if i == 0:
        return 0
    else:
        return i - 1


def get_ferda_time(dt: datetime) -> str:
    time = int(dt.strftime("%H%M"))
    keys = list(ferda_time.keys())
    return ferda_time[keys[low_bound_bisect(keys, time)]]


def get_current_ferda_time() -> str:
    return get_ferda_time(datetime.now())


def pretty_print_ferda_time(dt: datetime) -> None:
    pretty_time = (
        f"{dt.astimezone().strftime('%I:%M %p')} | {get_ferda_time(dt)}"
    )
    print(pretty_time)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        pretty_print_ferda_time(datetime.now())
        exit(0)

    try:
        pretty_print_ferda_time(datetime.strptime(sys.argv[1], "%H:%M"))
    except ValueError:
        print(
            "Invalid time format. Please use 24-hour format.\n"
            "Example: 15:30"
        )