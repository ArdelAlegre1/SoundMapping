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

# def plot_time_series(data):
#     # only plotting x
#     length = data.shape[0]
#     fig = plt.figure(figsize = [20,10])
#     ax1 = fig.add_subplot(511)
#     ax1.plot(data[:,1], label='array 0')  # array 0
#     ax1.set_xlim(0,length)
#     ax1.set_ylim(-1,1)
#     ax1.legend()
#     ax2 = fig.add_subplot(512)
#     ax2.plot(data[:,4], label='array 1')  # array 1
#     ax2.set_xlim(0,length)
#     ax2.set_ylim(-1,1)
#     ax2.legend()
#     ax3 = fig.add_subplot(513)
#     ax3.plot(data[:,7], label='array 2')  # array 2
#     ax3.set_xlim(0,length)
#     ax3.set_ylim(-1,1)
#     ax3.legend()  
#     ax4 = fig.add_subplot(514)
#     ax4.plot(data[:,10], label='array 3') # array 3
#     ax4.set_xlim(0,length)
#     ax4.set_ylim(-1,1)
#     ax4.legend()
#     ax5 = fig.add_subplot(515)
#     ax5.plot(data[:,16], label='array 5') # array 5
#     ax5.set_xlim(0,length)
#     ax5.set_ylim(-1.,1.)
#     ax5.legend()
#     plt.xlabel('Time (samples)',fontsize='x-large')
#     plt.show()    

    
# def plot_time_series3(data, arrays_to_disp, options):
#     # only plotting x
#     length = data.shape[0]
#     num_array = len(arrays_to_disp)
#     fig = plt.figure(figsize = [20,10])
#     ax1 = fig.add_subplot(511)
#     ax1.plot(data[:,1], label='X, array 0')  # array 0
#     ax1.plot(data[:,2], label='Y, array 0')  # array 0
#     ax1.plot(data[:,3], label='Z, array 0')  # array 0
#     ax1.set_xlim(0,length)
#     ax1.set_ylim(-1,1)
#     ax1.legend()
#     ax2 = fig.add_subplot(512)
#     ax2.plot(data[:,4], label='X, array 1')  # array 1
#     ax2.plot(data[:,5], label='Y, array 1')  # array 0
#     ax2.plot(data[:,6], label='Z, array 1')  # array 0
#     ax2.set_xlim(0,length)
#     ax2.set_ylim(-1,1)
#     ax2.legend()
#     ax3 = fig.add_subplot(513)
#     ax3.plot(data[:,7], label='X, array 2')  # array 2
#     ax3.plot(data[:,8], label='Y, array 2')  # array 2
#     ax3.plot(data[:,9], label='Z, array 2')  # array 2
#     ax3.set_xlim(0,length)
#     ax3.set_ylim(-1,1)
#     ax3.legend()  
#     ax4 = fig.add_subplot(514)
#     ax4.plot(data[:,10], label='X, array 3') # array 3
#     ax4.plot(data[:,11], label='Y, array 3') # array 3
#     ax4.plot(data[:,12], label='Z, array 3') # array 3
#     ax4.set_xlim(0,length)
#     ax4.set_ylim(-1,1)
#     ax4.legend()
#     ax5 = fig.add_subplot(515)
#     ax5.plot(data[:,16], label='X, array 5') # array 5
#     ax5.plot(data[:,17], label='Y, array 5') # array 5
#     ax5.plot(data[:,18], label='Z, array 5') # array 5
#     ax5.set_xlim(0,length)
#     ax5.set_ylim(-1,1)
#     ax5.legend()
#     plt.show()