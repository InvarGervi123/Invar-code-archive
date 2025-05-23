import cv2
import pyautogui
import time
import numpy as np
from PIL import Image


cap = cv2.VideoCapture(0)

prev_position = None
last_action = time.time()
last_movement_time = time.time()

# אזור עבודה מתוך התמונה (למנוע רעש רקע)
ROI_TOP = 100
ROI_BOTTOM = 400
ROI_LEFT = 200
ROI_RIGHT = 500

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    roi = frame[ROI_TOP:ROI_BOTTOM, ROI_LEFT:ROI_RIGHT]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (21, 21), 0)
    _, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    biggest = None
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000 and area > max_area:
            max_area = area
            biggest = contour

    if biggest is not None:
        x, y, w, h = cv2.boundingRect(biggest)
        cx = x + w // 2
        cy = y + h // 2
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(roi, (cx, cy), 5, (0, 0, 255), -1)

        if prev_position is not None:
            dx = cx - prev_position[0]
            dt = time.time() - last_action

            # זיהוי תנועה משמעותית
            if dt > 2:
                if dx > 40:
                    print("▶️ Next track")
                    #pyautogui.press("nexttrack")
                    #last_action = time.time()
                elif dx < -40:
                    print("⏮️ Previous track")
                    #pyautogui.press("prevtrack")
                    #last_action = time.time()
                elif abs(dx) < 5 and time.time() - last_movement_time > 2:
                    print("⏸️ Pause / Play")
                    #pyautogui.press("playpause")
                    #last_action = time.time()
                    with Image.open("goodman.jpg") as im:
                        im.rotate(45).show()
                        time.sleep(500)
                        im.close

            if abs(dx) > 5:
                last_movement_time = time.time()

        prev_position = (cx, cy)

    # ציור המלבן של האזור
    cv2.rectangle(frame, (ROI_LEFT, ROI_TOP), (ROI_RIGHT, ROI_BOTTOM), (255, 0, 0), 2)
    frame[ROI_TOP:ROI_BOTTOM, ROI_LEFT:ROI_RIGHT] = roi
    cv2.imshow("Hand Gesture Control (No MediaPipe)", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
