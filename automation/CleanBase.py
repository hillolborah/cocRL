import pyautogui
import time
from utils import zoom_camera

print("Starting script")
time.sleep(3)

print("Zoom out")
zoom_camera(15, -500, 0.1)
time.sleep(1)

print("Eagle Artillery anchor point")
eagle_art_coords = pyautogui.locateCenterOnScreen(r'F:\cocRL\TempDir\EA3.png', confidence=0.8)
print(eagle_art_coords)
time.sleep(1)
pyautogui.moveTo(eagle_art_coords)
zoom_camera(17, +500, 0.1)

time.sleep(1)

print("Segment I")

#Bush Logic here

print("Segment II")

#Bush Logic here

print("End")