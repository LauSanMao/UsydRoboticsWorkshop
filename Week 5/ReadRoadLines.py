
import cv2
import numpy as np
#add mask 
#not done

frame = cv2.imread('lane_img.jpg')
edges = cv2.Canny(frame,400,600) # This uses the canny edge detector. The 100 and 200 are rather arbitrary parameters; the second should be larger than the first, play around to see what numbers work best for each image.


# Use the Canny again.

minLineLength=100
maxLineGap=10
edges = cv2.Canny(frame,100,200)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)


blankImage = np.zeros(frame.shape)

#draw the lines onto our blank image
for l in lines:
    for x1,y1,x2,y2 in l:
        cv2.line(blankImage,(x1,y1),(x2,y2),(0,255,0),3)



cv2.imshow("original", frame)
cv2.imshow("edges", edges)
cv2.imshow("lines", blankImage)
cv2.waitKey(-1)
