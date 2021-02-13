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

"""
Returns the column indices of the DOA_points corresponding to the tuple of array numbers given, as a numpy array

:param comb: array numbers of combination
:type comb: tuple

:return: numpy array of all indices corresponding to array numbers
"""    
def get_indices_from_combination(comb):
    
    ind_list = []   
    for i in comb:
        for j in range(i*3, (i*3)+3):
            ind_list.append(j)
            
    return (np.asarray(ind_list))

"""
Takes in the matrix determined using a subset of calibration points, and a tuple indicating which arrays were active.
Returns a padded matrix with 0's in the missing positions.

:param mat: input B matrix of size 2x(3k) where k indices the number of active matrices. Also k=len(which_arrays_active).
:type mat: numpy array
:param which_arrays_active: tuple of integers indicating the number of arrays active.
:type which_arrays_active: tuple
"""
def pad_linear_transform_matrix(mat, which_arrays_active):

    assert(mat.shape[0]==2)
    assert(mat.shape[1]==(len(which_arrays_active)*3))
    
    # which array is missing in which_arrays_active
    
    all_arrays = set([0,1,2,3,4])
    active_arrays = set(which_arrays_active)
    inactive_arrays = list(all_arrays - active_arrays)
    
    # we get our final matrix B by splitting up mat into subarrays of 2x3 - one for each array
    # for inactive arrays, we set the subarray to a zero array of shape 2x3 
    
    # 1. split       
    arr_num_map_B = {}
    for i in range(len(which_arrays_active)):
        indices_for_i = [i*3,(i+1)*3]
        arr_num_map_B[which_arrays_active[i]] = mat[:,indices_for_i[0]:indices_for_i[1]]
    
    for i in range(len(list(inactive_arrays))):
        empty_slice = np.zeros((2,3))
        arr_num_map_B[inactive_arrays[i]] = empty_slice
        
    # 2. join
    sorted_array_numbers = sorted(arr_num_map_B.keys())
    list_slices = []
    for i in sorted_array_numbers:
        list_slices.append(arr_num_map_B[i])
    fin_mat = np.hstack(list_slices)
    
    return(fin_mat)