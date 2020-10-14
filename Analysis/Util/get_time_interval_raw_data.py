import datetime
import numpy as np
import pandas as pd
import sys
import time
sys.path.append('/home/ardelalegre/SoundMapping/Database/Tables')
from RawService import RawService

rawService = rawService()

#TODO move to general util file
def strTime_to_unixTime(start, end):
    FORMAT_TIMESTRING = '%b %d %Y %I:%M%p'
    dt_start = datetime.datetime.strptime(start, FORMAT_TIMESTRING)
    dt_end = datetime.datetime.strptime(end, FORMAT_TIMESTRING)
    unixtime_start = time.mktime(dt_start.timetuple())
    unixtime_end = time.mktime(dt_end.timetuple())
    return unixtime_start, unixtime_end    

"""
Gets numpy dataset from multiDimMatrix

@param String start_time - start date and time: Sep 28 2020 11:30AM
@param String end_time - end date and time: Sep 28 2020 11:30AM

@return numpy matrix of coordinate and time data
"""
def get_time_interval_raw_data(start_time, end_time):

    #convert time to unix time
    unixtime_start, unixtime_end = strTime_to_unixTime(start_time, end_time)
    
    #get data from multiDimMatrix
    dataObj = rawService.get_time_interval_object(unixtime_start, unixtime_end)
    
    dataPoints = dataObj.fetchall()
    df = pd.DataFrame(dataPoints)
    df.columns = dataPoints[0].keys() 
    df = df.fillna(value=np.nan)
    
    return df.to_numpy()  