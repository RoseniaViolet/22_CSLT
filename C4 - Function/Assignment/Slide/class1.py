# # In leen man hinh tong cac so nguyen duong le trong n so nguyen duong dau tien
# # Ham tong n
# vd Tong(10)
# tong = 25
def nhap():
    n = int(input())
    return n
def Tinh(n):
    S = 0
    for i in range(1,n+1):
        if i % 2 == 1 :
            S += i
    return S
def InKQ(n,S):
    print(f'Tong cua {n} cac so nguyen duong le la {S} ')
n = nhap()
S= Tinh(n)
InKQ(n,S)