def Nhap():
    L = []
    for _ in range(10):
        n = int(input())
        L.append(n)
    x = int(input('x='))
    return L,x
def CauA(L,x):
    for i in range(len(L)):
        if L[i]==5:
            L[i]=x
    InKq(L)
def CauB(L,x):
    i = 0
    while i < len(L):
        if L[i] == x:
            del(L[i])
        else:
            i += 1
    InKq(L)
def InKq(L):
    for x in L:
        print(x,end=', ')


L,x=Nhap()
CauB(L,x)
    