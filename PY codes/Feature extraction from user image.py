import os
import numpy as np
import cv2
from PIL import Image
lbphrecognizer = cv2.face.LBPHFaceRecognizer_create()
path="PATH to Listing 1 result line 12 *.png"
def getImagesWithID(path):
    faceimagePaths = [os.path.join(path, f) for f in os.listdir(path)]   
    faces = []
    IDs = []
    for faceimagePath in faceimagePaths:      
        facesImg = Image.open(faceimagePath).convert('L')
        faceNP = np.array(facesImg, 'uint8')
        ID= int(os.path.split(faceimagePath)[-1].split(".")[1])
        faces.append(faceNP)
        IDs.append(ID)
        cv2.imshow("Adding faces for traning",faceNP)
        cv2.waitKey(10)
    return np.array(IDs), faces
Ids,faces  = getImagesWithID(path)
lbphrecognizer.train(faces,Ids)
lbphrecognizer.save("PATH to save result *.xml")
cv2.destroyAllWindows()
