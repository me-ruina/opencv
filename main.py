import cv2

# Read the video
cap = cv2.VideoCapture(0)

# Read the first frameй
ret, frame = cap.read()
def take_frame():


# Initialize the tracker
tracker = cv2.legacy.TrackerMedianFlow_create()
tracker.init(frame, (x, y, w, h))
while True:
    ret, frame = cap.read()
    if not ret:
        break
    while True:
        if cv2.waitKey(1) & 0xFF == ord("s"):
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
            tracker = cv2.legacy.TrackerMedianFlow_create()
            ret, track_window = tracker.update(frame)
            x, y, w, h = int(track_window[0]), int(track_window[1]), int(track_window[2]), int(track_window[3])
            img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow('frame', img2)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
