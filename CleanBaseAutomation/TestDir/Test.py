import cv2
import numpy as np
import mss
from ultralytics import YOLO
import time

# -------- CONFIG --------
MODEL_PATH = r"F:\cocRL\CleanBaseAutomation\Yolov8Dir\runs\detect\yolov8m_vegetation_v8\weights\best.pt"
CONF = 0.4
IOU = 0.5
# ------------------------

# Load model
model = YOLO(MODEL_PATH)

time.sleep(3)
# Capture screen
with mss.mss() as sct:
    monitor = sct.monitors[2]  # primary screen
    screen = np.array(sct.grab(monitor))

# Convert to OpenCV format
frame = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)

# Run inference
results = model(frame, conf=CONF, iou=IOU, verbose=False)

# Visualize results
annotated = results[0].plot()

cv2.imshow("YOLO Screen Snapshot", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
