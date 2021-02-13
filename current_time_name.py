import load_schedule
from datetime import time
from time import ctime
def is_time_between(begin_time, end_time, check_time):
    begin_time_min_hr = begin_time.split(":")
    end_time_min_hr = begin_time.split(":")
    begin_time = time(int(begin_time_min_hr[0]), int(begin_time_min_hr[1]))
    end_time = time(int(end_time_min_hr[0]), int(end_time_min_hr[1]))
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:
        return check_time >= begin_time or check_time <= end_time

def generate_docname_time(timex):
    schedule = load_schedule.load_schedule()
    for key in schedule:
        for lession in schedule[key]:
            lession_formatted_times = lession[0].split("-")
            for time in lession_formatted_times:
                lession_formatted_times[lession_formatted_times.index(time)]
            print(is_time_between(lession_formatted_times[0], lession_formatted_times[1], time(10, 0)))
    
generate_docname_time(1)