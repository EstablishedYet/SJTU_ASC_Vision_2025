import cv2
import os

# Input video
video_path = r"E:\Downloads\QQ\mmexport1757826550812.mp4"
output_dir = r"E:\2024-2025summer\socialpractice\frames_"

# Create output folder if not exists
os.makedirs(output_dir, exist_ok=True)

# Open video
cap = cv2.VideoCapture(video_path)

frame_id = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # End of video
    
    # Save frame as image
    filename = os.path.join(output_dir, f"frame_{frame_id:04d}.jpg")
    cv2.imwrite(filename, frame)
    
    frame_id += 1

cap.release()
print(f"Extracted {frame_id} frames to '{output_dir}'")
