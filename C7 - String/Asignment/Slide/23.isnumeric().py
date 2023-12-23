while True:
    a = (input('a='))
    b = (input('b='))
    if  a.isdecimal() and b.isdecimal():
        tong = int(a)+int(b)            
        print(f'a+b={tong}')
        break
    else:
        print('Yêu cầu nhập lại')
        
        
# def NhapSo(thongbao):
#     print(thongbao)
#     while True:
#         x=input()
#         if x.isnumeric():
#             return int(x)
#         else:
#             print("Khong hop le!!!")


# a=NhapSo("Nhap so nguyen a:")
# b=NhapSo("Nhap so nguyen b:")
# print("a+b=",a+b)
