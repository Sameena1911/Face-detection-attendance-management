import cv2

#trained dataset
trainedDataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#read a image
img = cv2.imread('images/img2.jpg')

#convert to gray scale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=trainedDataset.detectMultiScale(gray)
print(faces)
for x,y,width,height in faces:
    cv2.rectangle(img, (x,y), (x+width,y+height), (255,0,0), 2)
cv2.imshow('sameena',img)
#cv2.imshow('Gray',gray)
cv2.waitKey()