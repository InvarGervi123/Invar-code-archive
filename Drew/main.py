from PIL import Image

def image_to_ascii(image_path, output_width=200, output_file="ascii_art.txt"):
    # Открытие изображения и преобразование в черно-белое
    image = Image.open(image_path).convert('L')

    # Определение размеров изображения
    width, height = image.size

    # Вычисление соотношения сторон и масштабирование изображения для заданной ширины
    aspect_ratio = height / float(width)
    output_height = int(output_width * aspect_ratio)
    resized_image = image.resize((output_width, output_height))

    # Определение символов для ASCII art (более детализированный набор)
    ascii_chars = "@B%W#*oahkbdpwmZO0QCJYXzcvnxrjft/\|()1{}[]-_+~<>i!lI;:,\"^`'. "

    # Преобразование каждого пикселя в символ ASCII
    ascii_art = ""
    for y in range(output_height):
        for x in range(output_width):
            pixel_value = resized_image.getpixel((x, y))
            ascii_art += ascii_chars[pixel_value * len(ascii_chars) // 256]
        ascii_art += "\n"

    # Сохранение ASCII art в текстовый файл
    with open(output_file, "w") as file:
        file.write(ascii_art)

if __name__ == "__main__":
    input_image_path = "IMG-20220323-WA0000.jpg"
    output_ascii_file = "ascii_art.txt"
    image_to_ascii(input_image_path, output_width=720, output_file=output_ascii_file)
    print("ready")