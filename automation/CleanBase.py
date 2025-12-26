import pyautogui
import time

from utils import locate_ui_element

time.sleep(3)

print("Vegetation count script:")


# bush_img = locate_ui_element(r'F:\cocRL\assets\Vegetation\Bush1.png', confidence=0.5)  
# bush_coord = pyautogui.locateAllOnScreen('F:\cocRL\assets\Vegetation\Bush1.png', confidence=0.5)
# print(bush_coord)

# bush_coords = list(pyautogui.locateAllOnScreen(
#     r'F:\cocRL\assets\Vegetation\Bush1.png',
#     confidence=0.5
# ))

# print(bush_coords)
# print("Bush count:", len(bush_coords))

# count = 0
# for bush in pyautogui.locateAllOnScreen(
#         r'F:\cocRL\assets\Vegetation\Bush3.png',
#         confidence=0.85):
#     print(bush)
#     count += 1

# print("Bush count:", count)


bush_coor = pyautogui.locateCenterOnScreen(r'F:\cocRL\assets\Vegetation\EagleArtillery.png', confidence=0.85)
print(bush_coor)

print("End")

