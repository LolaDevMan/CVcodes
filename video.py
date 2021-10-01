import numpy as np
import cv2
import argparse
from collections import deque

linecolor = (100, 215, 255)
cap = cv2.VideoCapture(0)
pts = deque(maxlen=7)
lwr_red = np.array([119, 191, 130])
upper_red = np.array([219, 254, 254])
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.inRange(hsv, lwr_red, upper_red)
    mask = cv2.dilate(mask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 5:
            cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 255), 2)
            cv2.circle(frame, center, 5, linecolor, -1)
    pts.append(center)
    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue
        thick = 3
        cv2.line(frame, pts[i - 1], pts[i], linecolor, thick)

    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30)
    if key == 32:
        break

cap.release()
cv2.destroyAllWindows()




