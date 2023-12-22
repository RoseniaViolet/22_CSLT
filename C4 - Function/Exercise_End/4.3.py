import math

def nhap():
    print('Nhap 3 so nguyen:')
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    return a, b, c

def giaipt(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x1 = -b / (2*a)
        x2 = -b / (2*a)
        return x1, x2
    else:
        return None

def inkq(x1, x2):
    if x1 == x2:
        print('Phuong trinh co nghiem kep')
        print(f'x1=x2={x1}')
    else:
        print('Phuong trinh co hai nghiem')
        print(f'x1={x1}')
        print(f'x2={x2}')

a, b, c = nhap()
result = giaipt(a, b, c)
if result is not None:
    x1, x2 = result 
    inkq(x1, x2)
else:
    print('Phuong trinh vo nghiem')
