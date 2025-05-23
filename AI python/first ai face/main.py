import cv2
import numpy as np

# Загрузка каскадного классификатора для распознавания лиц
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if face_cascade.empty():
    raise IOError("Не удалось загрузить файл 'haarcascade_frontalface_default.xml'")

# Загрузка изображения для наложения (например, с эффектом цензуры)
# Рекомендуется использовать PNG с альфа-каналом для прозрачности
censor_img = cv2.imread('censor.png', cv2.IMREAD_UNCHANGED)
if censor_img is None:
    raise IOError("Не удалось загрузить файл 'censor.png'")

# Открываем видеопоток с вебкамеры
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Преобразуем кадр в оттенки серого для детекции лиц
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Обнаружение лиц на кадре
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Изменяем размер изображения для цензуры так, чтобы оно соответствовало размеру найденного лица
        overlay = cv2.resize(censor_img, (w, h), interpolation=cv2.INTER_AREA)
        
        # Если изображение для наложения имеет альфа-канал
        if overlay.shape[2] == 4:
            # Извлекаем цветное изображение и альфа-канал
            overlay_rgb = overlay[:, :, :3]
            alpha_mask = overlay[:, :, 3] / 255.0  # нормализуем альфа-канал в диапазоне [0,1]
        else:
            # Если альфа-канала нет – создаём маску, заполненную единицами
            overlay_rgb = overlay
            alpha_mask = np.ones((h, w), dtype=np.float32)
        
        # Определяем область интереса (ROI) на исходном кадре, куда будем накладывать изображение
        roi = frame[y:y+h, x:x+w]
        
        # Наложение overlay на ROI с учетом альфа-канала
        # Для каждого цветового канала выполняем смешивание
        for c in range(0, 3):
            roi[:, :, c] = (alpha_mask * overlay_rgb[:, :, c] +
                            (1 - alpha_mask) * roi[:, :, c])
        
        # Помещаем обновленную область обратно в кадр
        frame[y:y+h, x:x+w] = roi

    # Отображаем результат
    cv2.imshow("Censorship", frame)
    
    # Нажмите 'q', чтобы выйти из цикла
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
