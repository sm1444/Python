import numpy as np

a = np.array([[1,0,2,5],
             [0,4,5,6],
             [9,0,11,12],
             [14,0,16,13]])

zero_positions = np.where(a==0)
print(zero_positions)