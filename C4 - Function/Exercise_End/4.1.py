def nhap():
    while True:
        n = int(input('n='))
        if n >= 0:
            return n
def inkq(n):
    for i in range(2,n+1):
        if i % 2 == 0:
            print(f'{i} ',end='')
while True:
    n = nhap()
    inkq(n)
    print()
    Tieptuc = input('Tiep tuc khong?')
    if Tieptuc.upper == 'K':
        break