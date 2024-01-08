def LaSoNguyenTo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def SoHopLe(x):
    if x >= 1:
        return True
    else:
        return False

def NhapVaDem():
    kq = 0
    print("Nhap day so:")
    while True:
        try:
            x = int(input())
            if SoHopLe(x) == False:
                break
            if LaSoNguyenTo(x) == True:
                kq += 1
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return kq

def InKQ(kq):
    print(f"Co {kq} so nguyen to")

kq = NhapVaDem()
InKQ(kq)
