def Nhap():
    n = int(input('n='))
    while n not in range(2, 51):
        n = int(input('n='))
    return n
def Kiemtra(a):
    for i in range(2, a+1):
        if a % i == 0 and a != 2:
            print(f'{a} khong la SNT')
            break 
    else:
        print(f'{a} la SNT')
    return a
def Ketqua():
    a = Nhap()
    result = Kiemtra(a)
# Main code
Ketqua()
