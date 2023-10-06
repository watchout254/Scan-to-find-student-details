from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Dan/Desktop/qrcode/image6.png')
matokeo = decode(img)
print(matokeo)

