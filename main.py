import cv2

cap = cv2.VideoCapture('dvor1.mp4')
ret, frame = cap.read()
bbox = cv2.selectROI('Frame', frame, fromCenter=False, showCrosshair=True)
tracker = cv2.legacy.TrackerMedianFlow_create()
tracker.init(frame, bbox)
cap.release()
tracker.update(frame)
def capture_object_for_tracking(video_path):
    global cap, ret, frame, bbox, tracker

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        key = cv2.waitKey(1) & 0xFF

        if key == ord('r'):
            bbox = cv2.selectROI('Frame', frame, fromCenter=False, showCrosshair=True)
            tracker.init(frame, bbox)

        success, bbox = tracker.update(frame)

        if success:
            # Рисуем прямоугольник вокруг объекта
            (x, y, w, h) = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Frame', frame)

        # Остановка видео при нажатии клавиши 'q'
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

