def LaSNT(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def Xu_ly(L):
    for i in L:
        print(i,end=' ')
def SoTN(a,b):
    if a > 0 and b > 0:
        return True
    return False
def Nhap():
    while True:
        try:
            a = int(input())
            b = int(input()) 
        except:
            print('Dinh dang dau vao khong lop le')
        else:
            if SoTN(a,b) == True:
                if a <= b:
                    return a,b
                else:
                    print('So thu nhat lon hon so thu 2')
            else:
                print('Vui Long nhap cac so tu nhien')
#main code:
L =[]
a,b = Nhap()
for x in range(a,b+1):
    if LaSNT(x) == True:
        L.append(x)
Xu_ly(L)
