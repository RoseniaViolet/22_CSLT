def nhap():
    n = int(input())
    return n
n = nhap()
print(f'So nguyen da nhap {n}')

def Tong_hieu(x,y):
    return x+y , x-y
a,b = Tong_hieu(10,7)
print(a,b)