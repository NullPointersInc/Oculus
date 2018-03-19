import numpy as np
import cv2
import tensorflow as tf

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow("Oculus", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
