def Nhap():
    n = int(input('n='))
    while n not in range(2, 51):
        n = int(input('n='))
    return n
def Kiemtra(a):
    for i in range(2, a):
        if a % i == 0:
            return False  # a is not prime
    return True  # a is prime
def Ketqua():
    k = Nhap()
    result = Kiemtra(k)
    if result:
        print(f'{k} la SNT')
    else:
        print(f'{k} khong la SNT')
# Main code
Ketqua()