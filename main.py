import cv2


def capture_object_for_tracking(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    bbox = cv2.selectROI('Frame', frame, fromCenter=False, showCrosshair=True)
    tracker = cv2.legacy.TrackerMedianFlow_create()
    tracker.init(frame, bbox)

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


capture_object_for_tracking('dvor1.mp4')
