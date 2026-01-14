import cv2
import os
from pathlib import Path

# CONFIG
INPUT_DIR = "raw/raw_val"
OUTPUT_DIR = r"F:/cocRL/CleanBaseAutomation/Yolov8Dir/RawResized/images/val"
TARGET_W = 1280
TARGET_H = 1280
PAD_COLOR = (0, 0, 0)  # black

os.makedirs(OUTPUT_DIR, exist_ok=True)

for img_path in Path(INPUT_DIR).glob("*.*"):
    img = cv2.imread(str(img_path))
    if img is None:
        continue

    h, w = img.shape[:2]

    # scale while preserving aspect ratio
    scale = min(TARGET_W / w, TARGET_H / h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # compute padding
    pad_left = (TARGET_W - new_w) // 2
    pad_right = TARGET_W - new_w - pad_left
    pad_top = (TARGET_H - new_h) // 2
    pad_bottom = TARGET_H - new_h - pad_top

    padded = cv2.copyMakeBorder(
        resized,
        pad_top,
        pad_bottom,
        pad_left,
        pad_right,
        cv2.BORDER_CONSTANT,
        value=PAD_COLOR
    )

    out_path = Path(OUTPUT_DIR) / img_path.name
    cv2.imwrite(str(out_path), padded)

print("✅ Padding complete")
