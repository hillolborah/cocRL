import pyautogui
import time

from utils import locate_ui_element

time.sleep(3)

print("Vegetation count script:")


bush_img = locate_ui_element(r'F:\cocRL\assets\Vegetation\Bush1.png', confidence=0.5)  

print("End")
