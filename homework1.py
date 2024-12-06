import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

#requests - запросить данные с сайта и вывести их в консоль.z
response = requests.get('https://requests.readthedocs.io/en/latest/')
print(response.text)

#pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
image = Image.open("holodno.jpg")

# изменяем размер
image = image.resize((300, 599))
image.save("holodno_ochen.jpg")

#добавление надписи на картинке
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 30)
draw = ImageDraw.Draw(image)
draw.text((10, 10), "Holodno ochen'", font=font, fill=(255, 0, 0))
image.save("holodno_ochen.jpg")

#numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a + b # сложение массивов
print(result)
result = a * b
print(result) # умножение массивов
scalar = 10
result = a + scalar
print(result) # добавление скалярного значения






