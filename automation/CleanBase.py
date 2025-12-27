import pyautogui
import time

print("Starting script")
time.sleep(5)

eagle_art_coords = pyautogui.locateCenterOnScreen(r'F:\cocRL\TempDir\EA2.png', confidence=0.5)
print(eagle_art_coords)
time.sleep(2)
pyautogui.moveTo(eagle_art_coords)
print("End")