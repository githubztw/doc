import numpy as np

arr = np.array([0, 10, 20, 30, 40])
mask = np.array([True, True , True, False, True])
indices = np.array([0, 2])
print(arr[mask])
print(arr[mask][indices]) 
