from pyzbar.pyzbar import decode
from PIL import Image

image_2 = Image.open('C:/Users/Dan/Desktop/qrcode/image2.png')
matokeo = decode(image_2)
print(matokeo)

