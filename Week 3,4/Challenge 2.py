import cv2
import numpy as np


#reading images
img = cv2.imread("cutie.jpg")
cv2.imshow('Cutie', img)

 #scale it to 50%
scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

#Create a new image 
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized image", resized)

#find dimensions of image
dimensions=resized.shape

height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

#using circle() function to draw a circle on the given image
circled = cv2.circle(resized,(225,300),40,(225,0,0),thickness=2)
cv2.imshow('Circle',circled)

#pass through greyscale blur and canny layer
#convert to greyscale
greyscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey',greyscale)

#blur
blur=cv2.GaussianBlur(img,(9,9),cv2.BORDER_DEFAULT)
#ksize has to be odd numbers
cv2.imshow('Blur',blur)

#canny
canny=cv2.Canny(img,125,200)
cv2.imshow('Canny',canny)


#rotate image 45 degrees
#Rotation
def rotate(img, angle, rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,scale=1.0)
    dimensions =(width,height)

    return cv2.warpAffine(img,rotMat,dimensions)

rotated= rotate(img,-45)
cv2.imshow('Rotate',rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()