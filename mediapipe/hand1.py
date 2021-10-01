import cv2
import mediapipe as mp
import time


mpHands = mp.solutions.hands
hands = mpHands.Hands(False, 1, 0.75, 0.5)
mpDraw = mp.solutions.drawing_utils


imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = hands.process(imgRGB)
    

def findPosition(self, img, handNo=0, draw=True):
    
    flag = 0
    if results.multi_hand_landmarks:
        myHand = results.multi_hand_landmarks[handNo]
        for id, lm in enumerate(myHand.landmark):
            flag = 1
    return flag

