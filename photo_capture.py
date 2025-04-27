import cv2

def capture_vehicle_photo_from_video(video_path='traffic_video.mp4', save_name='vehicle_photo.jpg'):
    cap = cv2.VideoCapture(video_path)

    ret, frame = cap.read() 
    if ret:
        cv2.imwrite(save_name, frame)
        print("✅ Frame captured from video and saved as:", save_name)
    else:
        print("❌ Failed to read video frame.")
    
    cap.release()
