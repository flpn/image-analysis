import cv2
import numpy as np


video = cv2.VideoCapture(0)  # 0 is for the first web cam, 'filename.avi' for file

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
