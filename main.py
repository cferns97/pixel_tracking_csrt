from webcam import open_webcam
from tracker import initialize_tracker, track_object
import cv2

def main():
    cap = open_webcam()
    if cap is None:
        return

    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        cap.release()
        return

    # Initialize tracker
    tracker, bbox = initialize_tracker(frame)

    # Start tracking
    track_object(cap, tracker, bbox)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
