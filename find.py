import numpy as np
import cv2

frame = cv2.imread('red.jpeg')
lwr_red = np.array([164, 245, 175])
upper_red = np.array([184, 265, 255])

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
kernel = np.ones((5, 5), np.uint8)
mask = cv2.inRange(hsv, lwr_red, upper_red)
mask = cv2.dilate(mask, kernel, iterations=1)
res = cv2.bitwise_and(frame, frame, mask=mask)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
center = None

if len(cnts) > 0:
    c = max(cnts, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    print([x,y])

cv2.imshow("Frame", frame)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
    