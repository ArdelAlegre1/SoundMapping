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

"""
Extract observations where all arrays are active from interval matrix data. Excludes zeros and nans

@param interval_matrix_data
@param array_indices - a list of target arrays: [0,1,2,3,5]

@return numpy array - cleaned_data: all cleaned observations corresponding to target arrays without time column
@return numpy array - selected_raw_obs: a size reduced matrix data extracted from the original matrix data using clean data indices. 
"""
def extract_all_active_observations(interval_matrix_data, array_indices):
    # exclude time column
    observations = interval_matrix_data[:,1:]
    selected_obs = np.hstack([observations[:,i*3:i*3+3] for i in array_indices])
    cleaned_data = []
    ind = []
    for i in range(selected_obs.shape[0]):
        if not any(np.isnan(selected_obs[i,:])) and not any(selected_obs[i,:]==0):
            cleaned_data.append(selected_obs[i,:])
            ind.append(i)
    selected_raw_obs = interval_matrix_data[ind,:]        
    return  np.vstack(cleaned_data), selected_raw_obs