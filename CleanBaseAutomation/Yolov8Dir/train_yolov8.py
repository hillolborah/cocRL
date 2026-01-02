from ultralytics import YOLO

# def main():
#     # Load pretrained YOLOv8-n model
#     model = YOLO("yolov8n.pt")

#     # Train the model
#     model.train(
#         data="data.yaml",     # Path to data.yaml
#         imgsz=768,             # Input image size
#         epochs=100,            # Number of training epochs
#         batch=8,               # Batch size (reduce to 4 if OOM)
#         device=0,              # GPU id (0 for single GPU)
#         workers=4,             # Data loader workers
#         cache=True,            # Cache images/labels in RAM
#         project="runs/detect", # Output directory
#         name="yolov8n_vegetation_v0"
#     )


def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data="data.yaml",
        imgsz=896,              
        epochs=100,
        batch=8,               
        device=0,
        workers=8,              
        amp=True,               # mixed precision
        cache=True,             # disable if RAM bottleneck
        project="runs/detect",
        name="yolov8n_vegetation_v1"
    )

if __name__ == "__main__":
    main()

