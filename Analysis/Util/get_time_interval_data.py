import numpy as np
import pandas as pd
import sys
sys.path.append('/home/ardelalegre/SoundMapping/Database/Tables')
from MultiDimMatrixService import MultiDimMatrixService
from RawService import RawService
from Tools import *


#instantiate rawService
rawService = RawService()
#instantiate MultiDimMatrixService
multiDimMatrixService = MultiDimMatrixService()

"""
Gets numpy dataset from raw data table

@param String start_time - start date and time: Sep 28 2020 11:30AM
@param String end_time - end date and time: Sep 28 2020 11:30AM

@return numpy matrix of coordinates and time data
"""
def get_time_interval_raw_data(start_time, end_time):

    #convert time to unix time
    unixtime_start, unixtime_end = strTime_to_unixTime(start_time, end_time)
    
    #get data from rawService
    dataObj = rawService.get_time_interval_object(unixtime_start, unixtime_end)
    
    dataPoints = dataObj.fetchall()
    df = pd.DataFrame(dataPoints)
    df.columns = dataPoints[0].keys() 
    df = df.fillna(value=np.nan)
    
    return df.to_numpy(), df 
  
"""
Gets numpy dataset from multiDimMatrix

@param String start_time - start date and time: Sep 28 2020 11:30AM
@param String end_time - end date and time: Sep 28 2020 11:30AM

@return numpy matrix of coordinates and time data
"""
def get_time_interval_matrix_data(start_time, end_time):

    #convert time to unix time
    unixtime_start, unixtime_end = strTime_to_unixTime(start_time, end_time)
    
    #get data from multiDimMatrix
    dataObj = multiDimMatrixService.get_time_interval_object(unixtime_start, unixtime_end)
    
    dataPoints = dataObj.fetchall()
    df = pd.DataFrame(dataPoints)
    df.columns = dataPoints[0].keys() 
    df = df.fillna(value=np.nan)
    
    return df.to_numpy()  