# in len màn hình kết quả kiểm tra n co phai la so nguyen to hay không
# nếu n là số nguyên tố thì in thông báo là số nguyên tố còn lại thông báo không là số nguyên tố
def Kiemtra(a):
    for i in range(2, a):
        if a % i == 0:
            return False  # a is not prime
    return True  # a is prime
def Ketqua(x):
    result = Kiemtra(x)
    if result:
        print(f'{x} la SNT')
    else:
        print(f'{x} khong la SNT')
# Main code
Ketqua(10)
Ketqua(5)