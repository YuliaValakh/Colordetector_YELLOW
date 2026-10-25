import cv2
import numpy as np


lower = np.array([15, 150, 20])
upper = np.array([35, 255, 255])


video = cv2.VideoCapture(0)

while True:
    success, img = video.read()
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)
    colored_mask = np.zeros_like(img)

    colored_mask[mask > 0] = [255, 255, 255]

    cv2.imshow("Vid_MASK", colored_mask)
    cv2.imshow("VID_MAIN", img)
    if cv2.waitKey(0):
        break


video.release()







