import math
def nhap():
    print('Nhap 3 so nguyen:')
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    return a,b,c
def giaipt(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return x1,x2
    elif delta == 0:
        x1= -b /(2*a)
        x2= -b /(2*a)
        return x1,x2
    else:
        print(f'Phuong trinh vo nghiem')
def inkq(x1,x2):
    if x1==x2:
        print(f'x1=x2={x1}')
    else:
        print(f'x1={x1}')
        print(f'x2={x2}')
a,b,c = nhap()
kq = giaipt(a,b,c)
inkq(*kq)