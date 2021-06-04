#!/usr/bin/env python3

import cv2

# open the primary video camera (give your terminal window permissions to access camera when you first run this)
cap = cv2.VideoCapture(0)

while True:
    # read images from the camera
    success, img = cap.read()
    # display the image in a window named "image"
    cv2.imshow("image", img)
    # if pressing "q" while the display window is active, "quit" the program by breaking the while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

