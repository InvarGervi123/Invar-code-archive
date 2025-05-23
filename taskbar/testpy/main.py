import os
import time
import sys

# Функция для отображения прогресса
def print_progress_bar(iteration, total, length=50):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r|{bar}| {percent}% Complete')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write('\n')

# Функция для создания файлов
def create_files(num_files, directory='files'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(num_files):
        file_path = os.path.join(directory, f'file_{i+1}.txt')
        with open(file_path, 'w') as file:
            file.write(f'This is file number {i+1}')
        #time.sleep(0.1)  # Задержка для демонстрации прогресса
        print_progress_bar(i + 1, num_files)

# Указание количества файлов для создания
num_files_to_create = 313654

# Вызов функции для создания файлов
create_files(num_files_to_create)
