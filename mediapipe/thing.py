import cv2
import time
import os
import hand as htm
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalFingers = fingers.count(1)
        print(totalFingers)
        if totalFingers==0:
            h="stone"
            cv2.putText(img,h, (100,250), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if totalFingers==2:
            h='scissor'
            cv2.putText(img,h, (100,250), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if totalFingers==5:
            h='paper'
            cv2.putText(img,h, (100,250), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if totalFingers==1:
            h=''
            cv2.putText(img,h, (100,250), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if totalFingers==3:
            h=''
            cv2.putText(img,h, (100,250), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.rectangle(img, (50, 200), (300, 270), (0, 255, 0), 2)
    cv2.imshow("Win if you can", img)
    if cv2.waitKey(10)==97:
        cv2.destroyAllWindows()
        cap.release()
        break