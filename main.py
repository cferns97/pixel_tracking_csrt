import cv2
from webcam import open_webcam
from tracker import update_tracking, is_tracking
from mouse_handler import mouse_callback

def main():

    print("\n=== CSRT Object Tracker ===")
    print("Left-click an object to start tracking.")
    print("Left-click again to stop tracking.")
    print("Press 'q' to quit the application.")
    print("===========================\n")

    cap = open_webcam()
    if cap is None:
        return

    # Create a window and set the mouse callback function
    cv2.namedWindow("CSRT Tracker")
    cv2.setMouseCallback("CSRT Tracker", mouse_callback, param=cap)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if is_tracking():
            frame = update_tracking(frame)

        cv2.imshow("CSRT Tracker", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
