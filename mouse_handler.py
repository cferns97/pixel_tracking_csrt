import cv2
from tracker import start_tracking, stop_tracking, is_tracking

def mouse_callback(event, x, y, flags, param):
    """Handles mouse clicks to start/stop tracking."""
    cap = param

    # Read a single frame for initializing the tracker
    ret, frame = cap.read()
    if not ret:
        return

    if event == cv2.EVENT_LBUTTONDOWN:
        if is_tracking():
            stop_tracking()
        else:
            start_tracking(frame, x, y)
