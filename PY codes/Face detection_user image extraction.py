import cv2
faces_cascades = cv2.CascadeClassifier("PATH to haar based cascades classifier file: haarcascade_frontalface_default.xml ")
cap = cv2.VideoCapture(0)
id = input('Enter user ID')
sampleN=0;
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faces_cascades.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        sampleN=sampleN+1;
    cv2.imwrite('result destination PATH to save processed user image'+str(id)+ "." +str(sampleN)+ ".png", gray[y:y+h, x:x+w])
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.waitKey(100)
    cv2.imshow('img',img)
    cv2.waitKey(1)
    if sampleN > 20:
        break
cap.release()
cv2.destroyAllWindows()