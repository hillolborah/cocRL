import pyautogui
import time


# time.sleep(3)
# coords = pyautogui.locateCenterOnScreen(r'F:\cocRL\Test\img2.png', confidence=0.8)
# print(coords)
# time.sleep(3)
# pyautogui.moveTo(coords)

time.sleep(3)
x, y = pyautogui.locateCenterOnScreen(r'F:\cocRL\Test\img2.png', confidence=0.8)
print(x, y)
time.sleep(3)
pyautogui.moveTo(x, y)