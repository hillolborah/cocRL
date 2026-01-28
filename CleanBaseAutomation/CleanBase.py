import pyautogui
import time
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from automation.utils import zoom_camera
from VegetationCv import clear_vegetation_segment


print("Starting script")
time.sleep(3)

print("Zoom out")
zoom_camera(15, -500, 0.1)
time.sleep(1)

print("Eagle Artillery anchor point")
eagle_art_coords = pyautogui.locateCenterOnScreen(
    r'F:\cocRL\TempDir\EA4.png', confidence=0.75
)
print(eagle_art_coords)

if eagle_art_coords is None:
    print("Eagle Artillery not found")
    exit(1)

time.sleep(1)
pyautogui.moveTo(eagle_art_coords.x, eagle_art_coords.y, duration=0.2)
zoom_camera(17, +500, 0.1)

time.sleep(1)

# ---------- Segment I ----------
print("Segment I (Bottom Half)")

screen_width, screen_height = pyautogui.size()


pyautogui.moveTo(eagle_art_coords.x, 1, duration=0.4)

time.sleep(0.3)
zoom_camera(15, -500, 0.1)

# Vegetation Logic here (BOTTOM HALF)
print("Vegetation Logic")
time.sleep(1)
clear_vegetation_segment()

print("SegI end, re-detect and reanchor Eagle Artillery")

time.sleep(0.5)
eagle_art_coords = pyautogui.locateCenterOnScreen(
    r'F:\cocRL\TempDir\EA4.png', confidence=0.75
)

print("Re-detected EA:", eagle_art_coords)

if eagle_art_coords is None:
    print("Eagle Artillery not found during re-anchor")
    exit(1)

pyautogui.moveTo(eagle_art_coords.x, eagle_art_coords.y, duration=0.2)
zoom_camera(17, +500, 0.1)

time.sleep(1)


# ---------- Segment II ----------
print("Segment II (Top Half)")

pyautogui.moveTo(eagle_art_coords.x, screen_height - 2, duration=0.4)

time.sleep(0.3)
zoom_camera(15, -500, 0.1)

# Vegetation Logic here (TOP HALF)
print("Vegetation Logic")
time.sleep(1)
clear_vegetation_segment()


print("End")

