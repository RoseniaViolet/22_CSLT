def LaSoNguyenTo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def SoHopLe(x):
    if x <= 1:
        return False
    return True

def NhapVaDem():
    Dem = 0
    print('Nhap day so:')
    while True:
        x = int(input())
        if SoHopLe(x) == True:
            if LaSoNguyenTo(x) == True:
                Dem += 1
        else:
            return Dem

def InKQ(kq):
    print(f'Co {kq} so nguyen to')

# main code
kq = NhapVaDem()
InKQ(kq)

    