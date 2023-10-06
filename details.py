import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import sys

print(f"Welcome to Mukenya's School\n"
      "After filling in your detals, open your qr code scanner and scan the qr code to save your details")

name = input("Name: ")
reg_no = int(input("Registration Number: "))
course = input("Course: ")
dept = input("Department: ")
stu_details = print(f"{name},{reg_no},{course},{dept} is logged in")


image_2 = qrcode.make(stu_details)
cheki = qrcode.QRCode(version = 1, box_size = 10, border = 5)
cheki.add_data(stu_details)
cheki.make(fit = True)
image_2 = cheki.make_image(fill_color = "yellow", back_color = "blue" )
image_2.save('C:/Users/Dan/Desktop/qrcode/image2.png')

#To decode go to decode.py file


