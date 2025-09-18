import pyautogui
import time

from utils import locate_ui_element, click_element, zoom_out_camera

time.sleep(3)

# Locate the button on the screen
attack_button = locate_ui_element(r'F:\cocRL\assets\AttackButton.png', confidence=0.5)  

# if attack_button:
#     pyautogui.click(attack_button)
#     print("Attack button clicked.")
# else:
#     print("Attack button not found.")

click_element(attack_button, "Attack button")

time.sleep(2)

find_match_button = locate_ui_element(r'F:\cocRL\assets\FindMatchButton.png', confidence=0.8)
if click_element(find_match_button, "Find Match button"):
    print("Executing scroll down...")
    time.sleep(5)
    zoom_out_camera()

# if find_match_button:
#     pyautogui.click(find_match_button)
#     print("Find Match button clicked.")

#     print("Executing scroll down...")
#     time.sleep(5)
#     pyautogui.scroll(-10000)
# else:
#     print("Find Match button not found.")

