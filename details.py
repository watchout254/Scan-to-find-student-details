import qrcode
print(f"Welcome to Mukenya's School\n"
      "After filling in your detals, open your qr code scanner and scan the qr code to save your details")

def st
    name = input("Name? : ")
    reg_no = int(input("Registration Number: "))
    course = input("Course: ")
    dept = input("Department: ")
    print(f"{name},{reg_no},{course},{dept} is logged in")


image_2 = qrcode.make(stu_details())
cheki = qrcode.QRCode(version = 1, box_size = )

