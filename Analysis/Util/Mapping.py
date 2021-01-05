import numpy as np

"""
computes linear transformtion matrix that maps DOAs to room space coordinates

@param list points_list - a list of cleaned DOAs. Each element in the list contains measurements of one point
@param numpyArray coordinates - an array of room space coordinates that are stored in the same order as points in points_list  
@param int dim - mapping dimension

@return numpyArray B - linear transformation matrix
@return numpyArray R_mean - the mean of room space coordinates
@return numpyArray D_mean - the mean of DOA measurements
@return numpyArray D - a matrix of all DOA measurements, features by the number of observations
"""
def generate_linear_transform_matrix(points_list, coordinates, dim):
    num_points = len(points_list)
    len_list = [point.shape[0] for point in points_list]
    total_len = sum(len_list)
    # D
    # row: features, columns: observations
    D = np.vstack(points_list).T
    # R
    R = np.hstack([np.zeros((dim,len_list[i]))+coordinates[i,:dim].reshape(-1,1) for i in range(num_points)])
    # B
    R_mean = np.mean(R, axis=1).reshape(-1,1)
    D_mean = np.mean(D, axis=1).reshape(-1,1)
    # calculating moore penrose inverse
    D_inv = np.linalg.pinv(D-D_mean) 
    # obtaining linear transformation matrix
    B = (R - R_mean) @ D_inv 
    return B, R_mean, D_mean, D
