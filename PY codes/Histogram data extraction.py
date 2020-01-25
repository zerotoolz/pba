import cv2
import numpy as np
f = cv2.FileStorage("PATH to Listing 2 result *.xml or *.yaml", 0)
L = f.getNode("opencv_lbphfaces")
h = L.getNode("histograms")
hist0 = h.at(0).mat()
np.save("PATH to save directory to array *.npy", hist0) 
