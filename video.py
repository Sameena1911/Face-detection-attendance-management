import cv2
trainedDataset=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video=cv2.VideoCapture('videos/vdo.mp4')
while True:
    success,frame=video.read()
    if success==True:
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = trainedDataset.detectMultiScale(gray_image)
        for x, y, width, height in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
        cv2.imshow('video', frame)
        cv2.waitKey(1)
    else:
        print("Frame null")
        break