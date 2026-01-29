import time
import pyautogui
import numpy as np
import cv2
import mss
from ultralytics import YOLO

MODEL_PATH = r"F:\cocRL\CleanBaseAutomation\Yolov8Dir\runs\detect\yolov8m_vegetation_v8\weights\best.pt"
CONF_THRES = 0.8
IOU_THRES = 0.5
SETTLE_TIME = 1.0      
CLICK_DELAY = 1.0
MAX_ITERS = 1


model = YOLO(MODEL_PATH)

VEGETATION_CLASSES = {
    "bush",
    "tree_1",
    "tree_2",
    "fallen_trunk",
    "trunk_1",
    "trunk_2",
    "gem_box",
    "mushroom"
}


#Multi monitor setup, if single monitor, set sct.monitors[1]
sct = mss.mss()
MONITOR = sct.monitors[2]  


def clear_vegetation_segment(max_iters=MAX_ITERS):
    """
    Detects and clears vegetation on secondary monitor.
    Iteratively clicks detected objects until none remain.
    """

    clicked_centers = set()

    for iteration in range(max_iters):
        print(f"\n[Iteration {iteration + 1}] Stabilizing camera...")
        time.sleep(SETTLE_TIME)

        print("Screen Capture")
        screenshot = sct.grab(MONITOR)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        print("YOLO Inference...")
        results = model(frame, conf=CONF_THRES, iou=IOU_THRES, verbose=False)[0]
        time.sleep(1)

        if not results.boxes or len(results.boxes) == 0:
            print("No detections — segment clear")
            return

        print("Class Filtering...")
        vegetation_boxes = []
        for box in results.boxes:
            cls_id = int(box.cls[0])
            # cls_name = model.names[cls_id]
            cls_name = model.names[cls_id].lower()


            if cls_name in VEGETATION_CLASSES:
                vegetation_boxes.append(box)

        # print("Detected classes:")
        # for box in results.boxes:
        #     cls_id = int(box.cls[0])
        #     cls_name = model.names[cls_id]
        #     print(" -", cls_name)

        #     if cls_name in VEGETATION_CLASSES:
        #         vegetation_boxes.append(box)

        if not vegetation_boxes:
            print("No vegetation left in this segment")
            return

        print(f"Detected {len(vegetation_boxes)} vegetation items")

        # Sort Top -> Bottom
        vegetation_boxes.sort(key=lambda b: int(b.xyxy[0][1]))

 
        print("Start Clicking...")
        for box in vegetation_boxes:
            #Note: coordinates system is applicable to two monitor setup with coc running on secondary monitor.
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            key = (cx // 10, cy // 10)
            if key in clicked_centers:
                continue
            clicked_centers.add(key)

            #Dual monitor absolute coordinates
            abs_x = MONITOR["left"] + cx
            abs_y = MONITOR["top"] + cy

            #Single monitor setup
            # abs_x = cx
            # abs_y = cy

            print(f"Clicking vegetation at ({abs_x}, {abs_y})")
            print(f"Class: {model.names[int(box.cls[0])]}")
            pyautogui.moveTo(abs_x, abs_y, duration=0.15)
            pyautogui.click()
            #Remove logic goes here for prod
            print("Remove logic placeholder")
            time.sleep(CLICK_DELAY)

        time.sleep(0.4)

    print("Max iterations reached — exiting segment")

###Test Run Function
# def main():
#     print("Starting VegetationCv standalone mode")

#     time.sleep(3)

#     pyautogui.moveRel(10, 0, duration=0.2)
#     pyautogui.moveRel(-10, 0, duration=0.2)

#     print("Running vegetation Clicking on visible screen area")
#     clear_vegetation_segment()


# if __name__ == "__main__":
#     main()
