import cv2
img = cv2.imread("PATH to VC Listing 5 result *.png, line 18")
smooth = cv2.GaussianBlur(img,(5,5),0)
cv2.imwrite("PATH to save result *.png", smooth)