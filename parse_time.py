from datetime import time
import re
def parse_interval(interval:str):
    """
    :param: interval: a string:
    :return: time.time() objects
    """
    regex = "([01]?[0-9]|2[0-3]):[0-5][0-9][ ]*-[ ]*([01]?[0-9]|2[0-3]):[0-5][0-9]"
    r = re.compile(regex)
    m = re.search(r, interval)
    if not m:
        return False
    split_interval = interval.split("-")
    for index, string in enumerate(split_interval):
        split_interval[index] = string.strip()
    hrmn_start = split_interval[0].split(":")
    hrmn_end = split_interval[1].split(":")
    try:
        return (time(int(hrmn_start[0]), int(hrmn_start[1])), time(int(hrmn_end[0]), int(hrmn_end[1])))
    except Exception as e:
        return e