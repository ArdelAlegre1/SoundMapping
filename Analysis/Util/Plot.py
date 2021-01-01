from matplotlib import pyplot as plt
import numpy as np
from get_time_interval_data import *



"""
plots given data

@param numpyArray cdata - dataset to plot

@return null
"""
def plot_data(cdata,figsize_x=20,figsize_y=20,figscale=[-1.5,1.5,-1.5,1.5]):
    figure = plt.figure(figsize=(figsize_x,figsize_y))
    ax = figure.add_subplot(111)
    ax.scatter(cdata[:,0],cdata[:,1],marker='.',s=1,c=np.arange(cdata.shape[0]))
    plt.xlim(figscale[0],figscale[1])
    plt.ylim(figscale[2],figscale[3])
    
    
    
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