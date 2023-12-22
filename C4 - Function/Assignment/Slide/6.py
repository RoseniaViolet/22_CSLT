def nhap():
    print('Nhap mot so nguyen:')
    n = int(input('n='))
    return n
def tinh(n):
    S=0
    for x in range ( 1, n + 1):
         S= S + x
    return S
def InKq(n,S):
    print('Thong cua ',n,' so nguyen duong dau tien=',S,sep='')
#maincode
n = nhap()
S = tinh(n)
InKq(n,S)