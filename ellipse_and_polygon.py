import cv2
import numpy as np

img= np.ones((500, 500, 3),np.uint8)

img[:]= 255, 255, 255

(x, y) = (int(img.shape[1]/2), int(img.shape[0]/2))
ellipse= cv2.ellipse(img, (x,y), (100, 50), 0, 0, 360, (0,0, 255), -1 )

pts = np.array([[20,100],[70,160],[130,140],[70,50]], np.int32)

pts = pts.reshape((-1,1,2))

img = cv2.polylines(img,[pts],True,(0,0,0))

cv2.imshow("Image", img)
cv2.waitKey(0)