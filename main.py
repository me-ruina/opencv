import cv2
# Захват видеопотока с веб-камеры
cap = cv2.VideoCapture(0)

while True:
    # Считывание кадра с веб-камеры
    ret, frame = cap.read()

    if ret:
        # Отображение кадра в окне
        cv2.imshow('Webcam', frame)

    # Для завершения приложения нажмите 'q'
    if cv2.waitKey(1) & 0xFF == ord('s'):
        bbox = cv2.selectROI('Frame', frame, fromCenter=False, showCrosshair=True)
        tracker = cv2.legacy.TrackerMedianFlow_create()
        tracker.init(frame, bbox)
        while True:
            ret, frame = cap.read()
            if ret:
                success, bbox = tracker.update(frame)

            if success:
                # Рисуем прямоугольник вокруг объекта
                (x, y, w, h) = [int(v) for v in bbox]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow('Frame', frame)

            # Остановка видео при нажатии клавиши 'q'
            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break

# Освобождение ресурсов и закрытие окон
cap.release()
cv2.destroyAllWindows()
