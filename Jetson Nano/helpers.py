# Importing all module
import cv2
import numpy as np


def detect_blue_color():

# Specifying upper and lower ranges of color to detect in hsv format
    blue_lower = np.array([95, 150, 20]) 
    blue_upper = np.array([135, 255, 255])  # (These ranges will detect Yellow)

# Capturing webcam footage
    webcam_video = cv2.VideoCapture(0)

    while True:
        success, video = webcam_video.read()  # Reading webcam footage

    # Converting BGR image to HSV format
        img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

    # Masking the image to find our color
        blue_mask = cv2.inRange(img, blue_lower, blue_upper)

        mask_contours, hierarchy = cv2.findContours(
        blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Finding contours in mask image

    # Finding position of all contours
        if len(mask_contours) != 0:
            for mask_contour in mask_contours:
                if cv2.contourArea(mask_contour) > 500:
                    x, y, w, h = cv2.boundingRect(mask_contour)
                    cv2.rectangle(video, (x, y), (x + w, y + h),
                              (0, 0, 255), 3)  # drawing rectangle

        

        cv2.imshow("mask image", blue_mask)  # Displaying mask image

        cv2.imshow("window", video)  # Displaying webcam image

        cv2.waitKey(1)


detect_blue_color()