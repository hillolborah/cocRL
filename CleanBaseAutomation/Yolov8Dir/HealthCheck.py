import pandas as pd
from pathlib import Path

# ------------------ Helpers ------------------

def extract_version_number(path: str) -> str:
    """
    Extracts only the version number (e.g. v2) from:
    ...\\yolov8s_vegetation_v2\\results.csv
    """
    for part in Path(path).parts:
        if "_v" in part:
            return part.split("_v")[-1]
    return "?"

def load_last_epoch(csv_path: str):
    df = pd.read_csv(csv_path)
    return df.iloc[-1]

def pct_change(curr, prev):
    if prev == 0:
        return float("inf")
    return (curr - prev) / prev * 100


# ------------------ Paths ------------------

CURRENT_RUN = r"F:\cocRL\CleanBaseAutomation\Yolov8Dir\runs\detect\yolov8m_vegetation_v8\results.csv"
PREVIOUS_RUN = r"F:\cocRL\CleanBaseAutomation\Yolov8Dir\runs\detect\yolov8m_vegetation_v7\results.csv"

# ------------------ Load Data ------------------

curr = load_last_epoch(CURRENT_RUN)
prev = load_last_epoch(PREVIOUS_RUN)

curr_v = extract_version_number(CURRENT_RUN)
prev_v = extract_version_number(PREVIOUS_RUN)

# ------------------ Header ------------------

print("\n========== YOLO HEALTH CHECK ==========")
print(f"Current Version : v{curr_v}")
print(f"Previous Version: v{prev_v}")
print(f"Epoch           : {int(curr['epoch'])}")

# ------------------ Core Metrics ------------------

print("\n--- Core Detection Metrics ---")
print(f"Precision   : {curr['metrics/precision(B)']:.3f} "
      f"({pct_change(curr['metrics/precision(B)'], prev['metrics/precision(B)']):+.1f}%)")

print(f"Recall      : {curr['metrics/recall(B)']:.3f} "
      f"({pct_change(curr['metrics/recall(B)'], prev['metrics/recall(B)']):+.1f}%)")

print(f"mAP@50      : {curr['metrics/mAP50(B)']:.3f} "
      f"({pct_change(curr['metrics/mAP50(B)'], prev['metrics/mAP50(B)']):+.1f}%)")

print(f"mAP@50–95   : {curr['metrics/mAP50-95(B)']:.3f} "
      f"({pct_change(curr['metrics/mAP50-95(B)'], prev['metrics/mAP50-95(B)']):+.1f}%)")

# ------------------ Loss Landscape ------------------

print("\n--- Loss Landscape (Train → Val) ---")

def loss_line(name, t_key, v_key):
    gap = curr[v_key] - curr[t_key]
    print(
        f"{name:<10}: "
        f"{curr[t_key]:.3f} → {curr[v_key]:.3f} "
        f"(gap {gap:+.3f})"
    )

loss_line("Box", "train/box_loss", "val/box_loss")
loss_line("Class", "train/cls_loss", "val/cls_loss")
loss_line("DFL", "train/dfl_loss", "val/dfl_loss")

# ------------------ Training Signals ------------------

print("\n--- Training Signals ---")
print(f"Train Box Loss Δ : {pct_change(curr['train/box_loss'], prev['train/box_loss']):+.1f}%")
print(f"Val Box Loss Δ   : {pct_change(curr['val/box_loss'], prev['val/box_loss']):+.1f}%")

# ------------------ High-Level Verdict ------------------

print("\n--- Model Trajectory Verdict ---")

if curr['metrics/mAP50-95(B)'] > prev['metrics/mAP50-95(B)']:
    print("📈 Model improved vs previous version")
elif curr['metrics/mAP50(B)'] >= prev['metrics/mAP50(B)']:
    print("➖ Marginal improvement (plateauing)")
else:
    print("📉 Regression detected — investigate changes")

print("======================================\n")
