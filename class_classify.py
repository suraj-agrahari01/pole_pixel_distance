import torch
import cv2
from pathlib import Path

# Load the YOLOv5 model
# Use YOLOv5l (large model)
model = torch.hub.load("ultralytics/yolov5", "yolov5l")

# Video path
video_path = "elehant.mp4"  # Replace with your video file path

# Output directory
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# Class names in COCO dataset (YOLOv5 default training dataset)
class_names = model.names

# Get class ID for elephant (index 22 in COCO dataset)
elephant_class_id = 22

# Open video file
cap = cv2.VideoCapture(video_path)
frame_count = 0

# Prepare to write the video with detections
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out_video_path = output_dir / "detected_elephants.mp4"
out_video = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the frame
    results = model(frame)

    # Filter results to keep only detections of elephants
    elephant_detections = results.xyxy[0][results.xyxy[0]
                                          [:, 5] == elephant_class_id]

    # Render the detections on the frame
    results.render()
    detected_frame = results.ims[0]

    # Convert the detected_frame to BGR format as OpenCV uses BGR by default
    detected_frame = cv2.cvtColor(detected_frame, cv2.COLOR_RGB2BGR)

    # Save the frame with detections
    frame_output_path = output_dir / f"frame_{frame_count:04d}.jpg"
    cv2.imwrite(str(frame_output_path), detected_frame)

    # Initialize video writer if it's not done yet
    if out_video is None:
        h, w = detected_frame.shape[:2]
        out_video = cv2.VideoWriter(
            str(out_video_path), fourcc, cap.get(cv2.CAP_PROP_FPS), (w, h))

    # Write the frame to the output video
    out_video.write(detected_frame)

    # Crop and save each detected elephant
    for i, det in enumerate(elephant_detections):
        x1, y1, x2, y2, conf, cls = map(int, det[:6])
        cropped_elephant = detected_frame[y1:y2, x1:x2]
        cropped_img_path = output_dir / \
            f"frame_{frame_count:04d}_elephant_{i}.jpg"
        cv2.imwrite(str(cropped_img_path), cropped_elephant)

    frame_count += 1

# Release resources
cap.release()
out_video.release()

print("Detection, cropping, and saving complete.")
