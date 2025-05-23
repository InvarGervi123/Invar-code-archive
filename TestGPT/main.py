import tensorflow as tf
from tensorflow.keras import layers, models

# Загрузка данных MNIST
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Нормализация данных и преобразование в формат для нейросети
train_images, test_images = train_images / 255.0, test_images / 255.0

# Создание модели нейросети
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Преобразование 2D-изображения в 1D-вектор
    layers.Dense(128, activation='relu'),    # Полносвязный слой с 128 нейронами и функцией активации ReLU
    layers.Dropout(0.2),                    # Dropout слой для регуляризации (отключение 20% нейронов случайным образом)
    layers.Dense(10, activation='softmax')   # Выходной слой с 10 нейронами и функцией активации Softmax
])

# Компиляция модели
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Обучение модели
model.fit(train_images, train_labels, epochs=5)

# Оценка точности модели на тестовых данных
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(f"Точность на тестовых данных: {test_accuracy}")


from PIL import Image
import numpy as np

# Загрузка и преобразование изображения
image_path = "path/to/your/image.png"
image = Image.open(image_path).convert("L")  # Преобразование в черно-белый формат
image = image.resize((28, 28))              # Изменение размера до 28x28
image_array = np.array(image) / 255.0       # Преобразование в numpy-массив и нормализация

# Подготовка изображения для передачи в модель
input_image = image_array.reshape(1, 28, 28)

# Предсказание класса
predicted_class = model.predict(input_image)
predicted_class_idx = np.argmax(predicted_class)
print(f"Распознанный класс: {predicted_class_idx}")
