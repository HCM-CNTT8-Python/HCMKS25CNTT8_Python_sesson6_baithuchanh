#cau 1:
price = int(input("Nhap don gia san pham: "))
quantity = int(input("Nhap so luong san pham: "))
total_products = price * quantity

if total_products >= 1000000:
    total_products = total_products + total_products * 0.1
    print("Don hang cua ban duoc giam 10% ")
else:
    print("Don hang cua ban ko duoc giam 10%")
    
print("Tong tien ban phai thanh toan la: ", total_products)



