# automation/utils.py

import pyautogui
import time

def locate_ui_element(image_path, confidence):
    """
    Locate a UI element on the screen using template matching.

    Args:
        image_path (str): Path to the reference image.
        confidence (float): Matching confidence (0.0–1.0).

    Returns:
        (x, y) tuple of coordinates if found, else None.
    """
    try:
        coords = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        return coords
    except Exception as e:
        print(f"Error locating {image_path}: {e}")
        return None


def click_element(coords, description):
    """
    Clicks on given screen coordinates.

    Args:
        coords (tuple): (x, y) coordinates.
        description (str): Label for logging.

    Returns:
        bool: True if clicked successfully, False otherwise.
    """
    if coords:
        pyautogui.click(coords)
        print(f"{description} clicked at {coords}.")
        return True
    else:
        print(f"{description} not found.")
        return False

def zoom_out_camera(scrolls=10, amount=-500, delay=0.1):
    """Scrolls the mouse wheel to zoom out the game camera."""
    for _ in range(scrolls):
        pyautogui.scroll(amount)
        time.sleep(delay)

# def hover_mouse_on()
