from matplotlib import pyplot as plt
import numpy as np
from get_time_interval_data import *

"""
queries raw matrix based on time strings. Given a mic number, it plots activity from all 4 channels.

@param string start_time_string - start time string of query
@param string end_time_string - end time string of query
@param int mic_number - microphone number for which to plot time series

@return null
"""
def plot_raw_time_series(start_time_string, end_time_string, mic_num):
    chairs_raw_np, df = get_time_interval_raw_data(start_time_string, end_time_string)
    only_array_1 = df.loc[df['Microphone Number'] == mic_num]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    only_array_1.plot(x='index', y='X_0', ax=ax)
    only_array_1.plot(x='index', y='X_1', ax=ax)
    only_array_1.plot(x='index', y='X_2', ax=ax)
    only_array_1.plot(x='index', y='X_3', ax=ax)
    ax.set_title('Raw time series plot. X_n indicates the nth channel')

 
"""
plot DOAs vs. time from selected arrays for all three coordinates. This function will use data from the orignal matrix data which contains a time column and all six arrays.

@param string start_time_string - start time string of query
@param string end_time_string - end time string of query
@param int mic_number - microphone number for which to plot time series

@return null
"""
def plot_doa_time_series(time_interval_matrix_data, arrays_to_disp):
    data = time_interval_matrix_data
    length = data.shape[0]
    num_array = len(arrays_to_disp)
    fig = plt.figure(figsize = [20,10])
    for i in range(0,num_array):
        ax = fig.add_subplot(num_array,1,i+1)
        array_label = 'array {}'.format(arrays_to_disp[i])
        ax.plot(data[:,arrays_to_disp[i]*3+1], label=array_label+' X')
        ax.plot(data[:,arrays_to_disp[i]*3+2], label=array_label+' Y')
        ax.plot(data[:,arrays_to_disp[i]*3+3], label=array_label+' Z') 
        ax.set_xlim(0,length)
        ax.set_ylim(-1,1)
        ax.legend()

    plt.show()