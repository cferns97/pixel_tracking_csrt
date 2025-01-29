import cv2

# Global variables
tracker = None
bbox = None
tracking = False

def start_tracking(frame, x, y):
    """Starts tracking with a bounding box centered around (x, y)."""
    global tracker, bbox, tracking

    box_size = 100
    bbox = (max(0, x - box_size // 2), max(0, y - box_size // 2), box_size, box_size)

    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, bbox)
    tracking = True
    print(f"Tracking started at: {bbox}")

def stop_tracking():
    """Stops tracking."""
    global tracker, tracking
    tracker = None
    tracking = False
    print("Tracking stopped.")

def update_tracking(frame):
    """Updates the tracker and draws the bounding box if tracking."""
    global tracker, bbox, tracking

    if tracker is not None:
        success, bbox = tracker.update(frame)
        if success:
            x, y, w, h = map(int, bbox)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame

def is_tracking():
    """Returns True if tracking is active."""
    return tracking
