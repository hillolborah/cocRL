import pandas as pd

df = pd.read_csv(r"F:\cocRL\CleanBaseAutomation\Yolov8Dir\runs\detect\yolov8n_vegetation_v1\results.csv")

last = df.iloc[-1]
# print(f"mAP50: {last['metrics/mAP50(B)']:.3f}")
# print(f"mAP50-95: {last['metrics/mAP50-95(B)']:.3f}")
# print(f"Precision: {last['metrics/precision(B)']:.3f}")
# print(f"Recall: {last['metrics/recall(B)']:.3f}")

print("===== YOLO Health Check =====")
print(f"Epoch: {last['epoch']}")

# Losses
print(f"Train Box Loss: {last['train/box_loss']:.3f}")
print(f"Train Class Loss: {last['train/cls_loss']:.3f}")
print(f"Train DFL Loss: {last['train/dfl_loss']:.3f}")
print(f"Validation Box Loss: {last['val/box_loss']:.3f}")
print(f"Validation Class Loss: {last['val/cls_loss']:.3f}")
print(f"Validation DFL Loss: {last['val/dfl_loss']:.3f}")

# Metrics
print(f"Precision: {last['metrics/precision(B)']:.3f}")
print(f"Recall: {last['metrics/recall(B)']:.3f}")
print(f"mAP50: {last['metrics/mAP50(B)']:.3f}")
print(f"mAP50-95: {last['metrics/mAP50-95(B)']:.3f}")

# Optional: Class-wise mAP (if present)
class_map_cols = [c for c in df.columns if "metrics/mAP50(B)" in c and c != "metrics/mAP50(B)"]
if class_map_cols:
    print("\nClass-wise mAP50:")
    for col in class_map_cols:
        class_name = col.split("/")[-1].replace("(B)", "")
        print(f"{class_name}: {last[col]:.3f}")

print("================================")