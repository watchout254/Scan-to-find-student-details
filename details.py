import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

print(f"Welcome to Mukenya's School\n"
      "After filling in your detals, open your qr code scanner and scan the qr code to save your details")

data = {}

name = input("Name: ")
reg_no = int(input("Registration Number: "))
course = input("Course: ")
dept = input("Department: ")

data[name] = reg_no, course, dept

img = qrcode.make(data)
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color = "blue", back_color = "white" )
img.save('C:/Users/Dan/Desktop/qrcode/image6.png')

print("You can now scan the code. Thank you my g...")





 
