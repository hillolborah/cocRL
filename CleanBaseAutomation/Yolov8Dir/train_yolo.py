from ultralytics import YOLO

def main():
    # # Load pretrained YOLOv8-n model
    # model = YOLO("yolov8n.pt")

    # # Train the model
    # model.train(
    #     data="data.yaml",     # Path to data.yaml
    #     imgsz=768,             # Input image size
    #     epochs=100,            # Number of training epochs
    #     batch=8,               # Batch size (reduce to 4 if OOM)
    #     device=0,              # GPU id (0 for single GPU)
    #     workers=4,             # Data loader workers
    #     cache=True,            # Cache images/labels in RAM
    #     project="runs/detect", # Output directory
    #     name="yolov8n_vegetation_v0"
    # )


    # # Train the model
    # model.train(
    #     data="data.yaml",     
    #     imgsz=960,             
    #     epochs=120,            
    #     batch=12,               
    #     device=0,              
    #     workers=4,             
    #     cache=True,            
    #     project="runs/detect", 
    #     name="yolov8n_vegetation_v1"
    # )


    # model = YOLO("yolov8s.pt")   

    # model.train(
    #     data="data.yaml",
    #     imgsz=960,               
    #     epochs=100,            
    #     batch=8,                 
    #     device=0,
    #     workers=8,
    #     amp=True,
    #     cache=True,
    #     project="runs/detect",
    #     name="yolov8s_vegetation_v2"
    # )

#     model.train(
#     data="data.yaml",
#     imgsz=768,
#     epochs=80,
#     batch=6,
#     device=0,
#     workers=8,
#     amp=True,
#     cache=False,
#     mosaic=0.5,
#     mixup=0.1,
#     scale=0.5,
#     degrees=10.0,
#     translate=0.1,
#     fliplr=0.5,
#     freeze=10,
#     patience=20,
#     project="runs/detect",
#     name="yolov8s_vegetation_v3"
# )

    # model.train(
    #     data="data.yaml",
    #     imgsz=768,
    #     batch=6,
    #     epochs=100,
    #     patience=30,
    #     device=0,
    #     workers=8,
    #     amp=True,
    #     freeze=10,              
    #     mosaic=0.4,             
    #     mixup=0.05,             
    #     close_mosaic=15,
    #     lr0=0.008,
    #     lrf=0.01,
    #     momentum=0.937,
    #     weight_decay=0.0007,
    #     box=6.0,
    #     cls=0.6,
    #     dfl=1.5,
    #     label_smoothing=0.05,
    #     cache=False,            
    #     project="runs/detect",
    #     name="yolov8s_vegetation_v4"
    # )

    # model = YOLO("yolov8m.pt")

    # model.train(
    #     data="data.yaml",
    #     imgsz=960,
    #     batch=6,
    #     epochs=120,
    #     patience=40,
    #     device=0,
    #     workers=8,
    #     amp=True,
    #     mosaic=0.6,
    #     mixup=0.0,
    #     close_mosaic=10,
    #     lr0=0.01,
    #     lrf=0.01,
    #     momentum=0.937,
    #     weight_decay=0.0005,
    #     box=7.0,
    #     cls=0.5,
    #     dfl=1.5,
    #     cache=False,
    #     project="runs/detect",
    #     name="yolov8m_vegetation_v5"
    # )

    # model = YOLO("runs/detect/yolov8m_vegetation_v5/weights/best.pt")

    # model.train(
    #     data="data.yaml",
    #     imgsz=896,
    #     batch=6,
    #     epochs=60,
    #     patience=20,
    #     device=0,
    #     workers=8,
    #     amp=True,
    #     mosaic=0.2,
    #     close_mosaic=5,
    #     mixup=0.0,
    #     box=8.0,
    #     cls=0.5,
    #     dfl=1.2,
    #     lr0=0.003,
    #     lrf=0.001,
    #     cache=False,
    #     project="runs/detect",
    #     name="yolov8m_vegetation_v6"
    # )

    # model = YOLO("runs/detect/yolov8m_vegetation_v6/weights/best.pt")

    # model.train(
    #     data="data.yaml",
    #     imgsz=896,
    #     batch=6,
    #     epochs=90,
    #     patience=0,
    #     device=0,
    #     workers=8,
    #     amp=True,
    #     mosaic=0.2,
    #     close_mosaic=5,
    #     mixup=0.0,
    #     box=8.0,
    #     cls=0.7,
    #     dfl=1.2,
    #     lr0=0.003,
    #     lrf=0.002,
    #     warmup_epochs=5,
    #     cache=False,
    #     project="runs/detect",
    #     name="yolov8m_vegetation_v7"
    # ) 

    # model = YOLO("runs/detect/yolov8m_vegetation_v7/weights/best.pt")

    # model.train(
    #     data="data.yaml",
    #     imgsz=896,
    #     batch=6,
    #     epochs=60,
    #     patience=0,
    #     device=0,
    #     workers=8,
    #     amp=True,
    #     mosaic=0.6,
    #     close_mosaic=10,
    #     mixup=0.15,
    #     copy_paste=0.2,
    #     box=6.0,       
    #     cls=1.1,       
    #     dfl=1.0,
    #     conf=0.001,
    #     lr0=0.002,
    #     lrf=0.0008,
    #     warmup_epochs=3,
    #     cache=False,
    #     project="runs/detect",
    #     name="yolov8m_vegetation_v8"
    # )

    model = YOLO("yolo11n.pt")

    model.train(
        data="data.yaml",
        imgsz=896,
        batch=6,
        epochs=60,
        patience=0,
        device=0,
        workers=8,
        amp=True,
        mosaic=0.6,
        close_mosaic=10,
        mixup=0.15,
        copy_paste=0.2,
        box=6.0,       
        cls=1.1,       
        dfl=1.0,
        conf=0.001,
        lr0=0.002,
        lrf=0.0008,
        warmup_epochs=3,
        cache=False,
        project="runs/detect",
        name="yolo11n_vegetation_v9"
    )

if __name__ == "__main__":
    main()

