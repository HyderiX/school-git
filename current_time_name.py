import load_schedule
from datetime import time
from time import ctime
import parse_time
def is_time_between(*args):
    """
    Returns true if check_time is between start_time and end_time
    :return: bool()
    """
    beginend_time, check_time = args
    begin_time, end_time = beginend_time
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:
        return check_time >= begin_time or check_time <= end_time

def generate_docname_time():
    schedule = load_schedule.load_schedule()
    for key in schedule:
        for lession in schedule[key]:
            print(is_time_between(parse_time.parse_interval(lession[0]), time(10, 0)))
generate_docname_time()