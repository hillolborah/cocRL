import pyautogui
import time

time.sleep(5)

# Locate the button on the screen (make sure 'attack_button.png' is saved)
attack_button = pyautogui.locateCenterOnScreen(r'F:\cocRL\assets\AttackButton.png', confidence=.5)

if attack_button:
    pyautogui.click(attack_button)
    print("Attack button clicked.")
else:
    print("Attack button not found.")

time.sleep(2)

find_match_button = pyautogui.locateCenterOnScreen(r'F:\cocRL\assets\FindMatchButton.png', confidence=.5)

if find_match_button:
    pyautogui.click(find_match_button)
    print("Find Match button clicked.")
else:
    print("Find Match button not found.")

