import cv2

def open_webcam():
    """Opens the webcam and returns the video capture object."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None
    return cap
