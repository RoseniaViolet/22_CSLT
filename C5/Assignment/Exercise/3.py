def nhap():
    L=[]
    x = int(input('x='))
    n = int(input('n='))
    for i in range(1,n+1):
         L.append(int(input()))
    return x,n,L
def Bai3(L,x):
    i = 0
    while i < len(L):
        if L[i] == x:
            del(L[i])
        else:
            i += 1
    return L
x,n,L = nhap()
print(Bai3(L,x))