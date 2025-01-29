import cv2

def initialize_tracker(frame):
    """Initializes the CSRT tracker with a bounding box in the center of the frame."""
    height, width, _ = frame.shape

    # Define the initial bounding box in the center
    box_width, box_height = 100, 100  # Box size
    x, y = (width // 2 - box_width // 2, height // 2 - box_height // 2)
    bbox = (x, y, box_width, box_height)

    # Create and initialize the CSRT tracker
    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, bbox)

    return tracker, bbox

def track_object(cap, tracker, bbox):
    """Tracks the object using the CSRT tracker and updates the bounding box."""
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Update the tracker
        success, bbox = tracker.update(frame)
        
        if success:
            # Draw the bounding box if tracking is successful
            x, y, w, h = map(int, bbox)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("CSRT Tracker", frame)

        # Press 'q' to exit the webcam window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
