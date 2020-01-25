import cv2
import numpy as np
f = cv2.FileStorage("C:\\Users\\Admin\\Desktop\\Datasets\\ibv\\anatoliy\\1_ibv.xml", 0)
L = f.getNode("opencv_lbphfaces")
h = L.getNode("histograms")
hist0 = h.at(0).mat()
np.save("PATH to Listing 2 result *.npy", hist0) 
