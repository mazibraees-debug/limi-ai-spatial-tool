import cv2
import json
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def analyze_room(image_path):

    img = cv2.imread(image_path)

    results = model(img)

    detected_classes = set()
    person_present = False

    for r in results:
        for i, box in enumerate(r.boxes):
            cls = int(r.boxes.cls[i])
            detected_classes.add(model.names[cls])
            if cls == 0:
                person_present = True

    brightness = img.mean()

    if brightness > 150:
        lighting = "Natural"
    elif brightness > 80:
        lighting = "Artificial"
    else:
        lighting = "Artificial Dim"

    if 'bed' in detected_classes:
        room_type = "Bedroom"
    elif any(cls in detected_classes for cls in ['desk', 'laptop', 'computer']):
        room_type = "Office"
    else:
        room_type = "Living Room"

    result = {
        "room_type": room_type,
        "lighting": lighting,
        "person_present": person_present
    }

    print(json.dumps(result))

    return result