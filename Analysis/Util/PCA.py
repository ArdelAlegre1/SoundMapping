from Models import *
from numpy import linalg as LA
import numpy as np
import sys
sys.path.append('/home/ardelalegre/SoundMapping/Analysis/Util')

"""
computes the eigen vectors and eigen values from given data

@param numpyArray data - data used to find eigen vectors and values

@return numpyArray eigen_values - array of eigen values
@return numpyArray eigen_vectors - array of eigen vectors
"""
def get_eigen_vectors(data):
    
    cdata, _ = get_cdata(data)
    dimensions = cdata.shape[1]
    n = cdata.shape[0]
    
    # calculate covariance matrix
    outters = np.zeros((dimensions, dimensions))
    for j in range(n):
        outters += np.outer(cdata[j,:], cdata[j,:])
    covariance = outters/n

    eigen_values, eigen_vectors = LA.eig(covariance)
    sorted_eig_val, sorted_eig_vec = sort_eigen_vectors(eigen_values, eigen_vectors)
   
    return sorted_eig_val, sorted_eig_vec


"""
computes normalized singular values from eigen vectors 

@param numpyArray data - eigen vectors

@return numpyArray singular_values 
"""
def eigen2singular(eigen_vectors):
    singular_values = np.sqrt(eigen_vectors)
    normalized = singular_values/np.sum(singular_values)
    return normalized


"""
calculates cdata from data

@param numpyArray data - cooridnate data points

@return cdata
@return data_mean
"""
def get_cdata(data):
    # data matrix does not contain time column
    if data.shape[1]%3 == 0:
        data_mean = np.nanmean(data, axis=0, keepdims=True)
        tmp = data - data_mean
        cdata=np.nan_to_num(tmp)
    # data matrix does contain time column
    else:      
        data_mean = np.nanmean(data[:,1:], axis=0, keepdims=True)
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
@param numpyArray eigen_values - array of eigen values
@param numpyArray eigen_vectors - array of eigen vectors

@return numpyArray data projected onto eigen vectors
"""
def project_to_eigen_vectors(data, dimensions, eigen_values, eigen_vectors):  
    return np.dot(data,eigen_vectors[:,:dimensions])