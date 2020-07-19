import cv2
import numpy as np

img= np.ones((500, 500, 3),np.uint8)

img[:]= 255, 255, 255

#drawing line
line = cv2.line(img, (0,0), (500, 500), (0,255,0), 3)

# calculating the  center of img
#drawing circle
(x, y) = (int(img.shape[1]/2), int(img.shape[0]/2))
circle = cv2.circle(img, (x,y), (120), (0, 0, 255), 4)

#drawing rectangle
rectangle = cv2.rectangle(img,(80, 80), (420, 420), (125, 125, 125), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)