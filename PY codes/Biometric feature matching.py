import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
threshold = 1.514 # set yourself to meet your requirement
x = np.load("PATH to reconstructed IBV after VC  result array *.npy")
y = np.load("PATH to CBV array *.npy")
z = euclidean_distances(x, y)
print("Result z = " + ("authenticated" if z <= threshold else "not authenticated"))