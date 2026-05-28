#cau 2:
password = 123456

for check in range(1, 4):
    check_passwork = input("Moi nhap mat khau: ")
    if check_passwork == password:
        print("Dang nhap thanh cong!")
        break
    else:
        print("Mat khau sai, vui long nhap lai!")

if check == 3:
    print("Tai khoang da bi khoa!")

# #cau 3:
total_quantity = int(input("Nhap tong so luong san pham: "))
valid_container = int(input("Nhap so thung hang hop le: "))