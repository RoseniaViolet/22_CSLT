def nhap():
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    return a,b,c
def max3(a,b,c):
    Max = max(a,b,c)
    return Max
def inkq(kq):
    print(f'So lon nhat la: {kq}')

# main code
a,b,c = nhap()
Max = max3(a,b,c)
inkq(Max)