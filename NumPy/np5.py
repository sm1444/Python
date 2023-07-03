import numpy as np

arr = np.array([[1,5,6],[4,7,2],[3,1,9]])

print("largest element: ",arr.max())
print("largest element: ",arr.max(axis=1)) #row index
print("largest element: ",arr.max(axis=0)) #column index
print("-----------------------")
print("smallest element: ",arr.min()) #column index
print("smallest element: ",arr.min(axis=1)) #column index
print("smallest element: ",arr.min(axis=0)) #column index
print("-----------------------")
print("Sum: ",arr.sum())
print("Sum: ",arr.sum(axis=1))
print("Sum: ",arr.sum(axis=0))