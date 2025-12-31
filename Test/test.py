import pyautogui
import time


# time.sleep(3)
# coords = pyautogui.locateCenterOnScreen(r'F:\cocRL\TempDir\Bush1.png', confidence=0.8)
# print(coords)
# time.sleep(3)
# pyautogui.moveTo(coords)

# time.sleep(3)
# x, y = pyautogui.locateCenterOnScreen(r'F:\cocRL\Test\img2.png', confidence=0.8)
# print(x, y)
# time.sleep(3)
# pyautogui.moveTo(x, y)

time.sleep(3)

matches = list(pyautogui.locateAllOnScreen(
    r'F:\cocRL\TempDir\Bush1.png', confidence=1
))

print(matches)

time.sleep(1)
