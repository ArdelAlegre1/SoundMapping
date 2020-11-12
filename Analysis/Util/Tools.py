import datetime
import time


"""
computes unix time from time string

@param string start - start time in string
@param string end - end time in string

@return float unixtime_start
@return float unixtime_end
"""
def strTime_to_unixTime(start, end):
    try:
        FORMAT_TIMESTRING = '%b %d %Y %I:%M%p'
        dt_start = datetime.datetime.strptime(start, FORMAT_TIMESTRING)
        dt_end = datetime.datetime.strptime(end, FORMAT_TIMESTRING)
    except ValueError:
        FORMAT_TIMESTRING = '%b %d %Y %I:%M:%S%p'
        dt_start = datetime.datetime.strptime(start, FORMAT_TIMESTRING)
        dt_end = datetime.datetime.strptime(end, FORMAT_TIMESTRING)
    unixtime_start = time.mktime(dt_start.timetuple())
    unixtime_end = time.mktime(dt_end.timetuple())
    return unixtime_start, unixtime_end   