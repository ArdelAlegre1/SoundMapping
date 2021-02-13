from numpy import linalg as LA
import numpy as np
import sys
sys.path.append('/home/ardelalegre/SoundMapping/Analysis/Util')
from Models import *

"""
computes the eigen vectors and eigen values from given data

@param numpyArray data - data used to find eigen vectors and values

@return numpyArray eigen_values - array of eigen values
@return numpyArray eigen_vectors = array of eigen vectors
"""
def get_eigen_vectors(data):
    
    cdata, _ = get_cdata(data)
    dimensions = cdata.shape[1]
    n=cdata.shape[0]
    block_size=10000
    
    # calculate covariance matrix
    outters = np.zeros((dimensions, dimensions))
    for j in range(n):
        outters += np.outer(cdata[j,:], cdata[j,:])
    covariance = outters/n

    eigen_values, eigen_vectors = LA.eig(covariance)
    sorted_eig_val, sorted_eig_vec = sort_eigen_vectors(eigen_values, eigen_vectors)
   
    return sorted_eig_val, sorted_eig_vec

"""
calculates cdata from data

@param numpyArray data - cooridnate data points

@return cdata
@return data_mean
"""
def get_cdata(data):
    # the first column of multi dimension matrix is time
    data_mean = np.nanmean(data[:,1:],axis = 0,keepdims = True)
    tmp = data[:,1:] - data_mean
    cdata=np.nan_to_num(tmp)
    
    return cdata, data_mean

"""
sorts eigen values and eigen vectors based on the magnitude of eigen values

@param numpyArray eigen_values
@param numpyArray eigen_vectors

@return sorted_eig_val
@return sorted_eig_vec
"""
def sort_eigen_vectors(eigen_values, eigen_vectors):
    eig_val_sorted_indices = np.argsort(eigen_values)
    eig_val_sorted_indices = eig_val_sorted_indices[-1::-1]
    sorted_eig_val = eigen_values[eig_val_sorted_indices]
    sorted_eig_vec = eigen_vectors[:,eig_val_sorted_indices]
    return sorted_eig_val, sorted_eig_vec


"""
projects data to eigen vectors

@param numpyArray cdata - data set to project to eigen vectors
@param int dimensions - number of eigen vectors to project data onto

if optional params are not set, default will be taken from values.py
@optionalParam numpyArray eigen_values - array of eigen values
@optionalParam numpyArray eigen_vectors - array of eigen vectors

@return numpyArray data projected onto eigen vectors
"""
def project_to_eigen_vectors(data, dimensions, eigen_values=EIGEN_VALUES, eigen_vectors=EIGEN_VECTORS):
        
    return np.dot(data,eigen_vectors[:,:dimensions])