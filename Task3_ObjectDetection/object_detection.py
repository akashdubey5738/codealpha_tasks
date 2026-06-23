# Task 3: Object Detection using YOLOv8
# CodeAlpha AI Internship - June 2026

from ultralytics import YOLO
import cv2

# Load pretrained YOLOv8 model
model = YOLO('yolov8n.pt')

print("=== Object Detection Tool ===")
print("Place an image named 'test.jpg' in same folder")

# Run detection on image
results = model('test.jpg')

# Show results
for r in results:
    print("Objects detected:", len(r.boxes))
    r.show()  # Opens image with boxes
    r.save(filename='output.jpg')  # Saves output

print("Detection complete! Check output.jpg")