def nhap():
    L=[]
    x = int(input('x='))
    y = int(input('y='))
    n = int(input('n='))
    for i in range(1,n+1):
         L.append(int(input()))
    return x,n,L,y
def Replace(L, x, y):
    for i in range(len(L)):
        if L[i] == x:
            L[i] = y
    return L
x,n,L,y = nhap()
print(Replace(L,x,y))

