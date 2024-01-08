def Nhap():
    a = float(input('a = '))
    b = float(input('b = '))
    x = input('ToanTu: ')
    return a, b, x

def KiemtraToanTu(x):
    return x in ['+', '-', '*', '/']

def TinhToan(a, b, x):
    kq = None  # Đặt giá trị mặc định cho kq
    if x == '+':
        kq = a + b 
    elif x == '-':
        kq = a - b
    elif x == '*':
        kq = a * b
    elif x == '/':
        try:
            kq = a / b
        except ZeroDivisionError:
            print('Khong the chia cho 0')
    return kq

# maincode
while True:
    a, b, x = Nhap()
    check = KiemtraToanTu(x)
    if check is True:
        kq = TinhToan(a, b, x)
        if kq is not None:
            print(f'{a} {x} {b} = {kq}')
    else:
        print('Toan tu khong hop le')
    TT = input('Tieptuc:')
    if TT.lower() != 't':
        break