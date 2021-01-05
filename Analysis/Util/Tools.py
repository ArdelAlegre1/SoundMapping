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


"""
returns the slice of matrix corresponding to start and end timestamps

@param ndarray - data with 0th column with time in seconds
@param string - start timestring with format '%b %d %Y %I:%M:%S%p'
@param string - end timestring with format '%b %d %Y %I:%M:%S%p'

@return int - index of first element of data with time greater than start
@return int - index of last element of data with time less than end
"""

def slice_interval_indices(data, start_timestring, end_timestring):
    
    format_timestring = '%b %d %Y %I:%M:%S%p' # setting format of input time
    
    # convert input timestrings to unix time
    
    start_standard_dt_string = datetime.datetime.strptime(start_timestring, format_timestring) 
    end_standard_dt_string = datetime.datetime.strptime(end_timestring, format_timestring)
    
    unix_start_timestring = datetime.datetime.timestamp(start_standard_dt_string)
    unix_end_timestring = datetime.datetime.timestamp(end_standard_dt_string)
    
    for x in range(data.shape[0]):
        if(data[x,0] > unix_start_timestring and data[x,0] < unix_end_timestring):
            start_index = x
            break
    for y in range(x,data.shape[0]):
        if(data[y,0] > unix_end_timestring):
            end_index = y
            break
    
    return(x,y)