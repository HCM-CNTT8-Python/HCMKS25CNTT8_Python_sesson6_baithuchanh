#cau 3:
total_quantity = 0
valid_container = 0


while True:
    quantity =int(input("Nhap so luong san pham: "))
    if quantity < 0:
        print("So luong ko hop le, bo qua thung nay!")
    elif quantity == 0:
        break
    else:
        total_quantity += quantity
        valid_container += 1

print("Tong so thung hang hop le: ", valid_container)
print("Tong so luong san pham thu duoc: ", total_quantity)
