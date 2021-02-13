import numpy as np

# table points
p1 = np.array([2.08, 1.81, 0.78])
p2 = np.array([3.45, 1.81, 0.78])
p3 = np.array([3.45, 2.57, 0.78])
p4 = np.array([2.08, 2.57, 0.78])
p5 = np.array([0.92, 1.71, 0.78])
p6 = np.array([0.92, 3.54, 0.78])
# chair points
p7 = np.array([0.450, 0.791, 0.5])
p8 = np.array([2.598, 1.567, 0.5]) 
p9 = np.array([3.544, 1.523, 0.5]) 
p10 = np.array([3.040, 3.120, 0.5]) 
p11 = np.array([1.266, 2.685, 0.5])

ROOM_COORDINATES = np.vstack([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11])