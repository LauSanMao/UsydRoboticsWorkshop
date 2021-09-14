import cv2
import numpy as np


#Challenge 3 Part 1 
img = cv2.imread('Faces/usrc_cropped.png')
cv2.imshow('Image',img)

# convert image to greyscale
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey',grey)

# Load picture frame
picFrame = cv2.imread('Faces/imageframe.png')

#store the haar face database to haarCascade
haarCascade=cv2.CascadeClassifier('haar_face.xml')

#detect a face and return the rectangular coordinates of the face
facesRect = haarCascade.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=5)

# Initialise face count
faceCount = 1

# paste frame onto face
for (x,y,w,h) in facesRect:
    faceROI = img[y:y+h,x:x+w,:]
    currentPicFrame = np.zeros((w+40,h+40,3))
    currentPicFrame = cv2.copyTo(picFrame,None)
    currentPicFrame = cv2.resize(currentPicFrame,(w+40,h+40))
    currentPicFrame[20:h+20, 20:w+20,:] = faceROI
    #cv2.imshow("framed_image", currentPicFrame)

    # Save image to folder
    cv2.imwrite('Week6_Framed/Image' + str(faceCount) + '.jpg', currentPicFrame)
    # Increase face count
    faceCount += 1

    cv2.waitKey(-1)
