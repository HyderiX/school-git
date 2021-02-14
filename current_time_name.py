import load_schedule
from datetime import time
from time import ctime
import parse_time
from datetime import datetime
import courses
import generate_name
import get_file_creation
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

def generate_docname_time(docname, string):
    date_time = datetime.fromtimestamp(get_file_creation.get_file_creation(docname))
    timex_string = date_time.strftime("%H:%M")
    day_created = courses.days_inv[date_time.strftime("%a")]
    timex = [int(timex_string.split(":")[0]), int(timex_string.split(":")[1])]
    schedule = load_schedule.load_schedule()
    for key in schedule:
        for lession in schedule[key]:
            if is_time_between(parse_time.parse_interval(lession[0]), time(timex[0], timex[1])) and key==day_created:
                print (generate_name.generate_docname(lession[1], string))
generate_docname_time("test.txt", "MeinHobby")