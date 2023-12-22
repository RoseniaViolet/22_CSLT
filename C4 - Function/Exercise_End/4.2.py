def nhap():
    n= int(input('n='))
    return n
def inkq(n):
    for i in range(2,n+1):
        if i % 2 == 0:
            print(f'{i} ',end='')
while True:
    n= nhap()
    inkq(n)
    print()
    TT=input('Tiep tuc khong?')
    if ( TT == 'K') or (TT=='k'):
        break