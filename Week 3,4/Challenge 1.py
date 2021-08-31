import cv2
import numpy as np


#reading images
img = cv2.imread("cutie.jpg")
cv2.imshow('Cutie', img)

#Read Video
capture = cv2.VideoCapture('kitten.mp4')
#VideoCapture(0) = Webcam input

#capture=cv2.VideoCapture(0)

while True:
    isTrue,frame=capture.read()
    #show frame
    cv2.imshow('',frame)

    #if the d key is pressed, kill screen
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()

cv2.waitKey(0)
cv2.destroyAllWindows()