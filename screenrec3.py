import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimension = (width, height)

x = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("A screen_recording2.avi", x, 30.0, dimension)

start_time = time.time()
duration = 60
end_time = start_time+duration
while True:
    img = pyautogui.screenshot()
    frame_1 = np.array(img)
    color = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(color)
    current_time = time.time()
    if current_time > end_time:
        break
output.release()
print("Screen Recorded Successfully......")
