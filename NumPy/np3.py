import numpy as np

arr = np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])

temp = arr[:2, ::2] #alternate rows and alternate columns
temp = arr[::2 ,::2]
print("temp: ",temp)

#indexing

temp=arr[[0,0,1,1],[0,1,2,3]]
print("temp: ",temp)

cond = arr>0
temp = arr[cond]
print("temp: ",temp)