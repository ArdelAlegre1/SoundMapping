from matplotlib import pyplot as plt
import numpy as np

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