def nhap():
    L=[]
    x = int(input('x='))
    n = int(input('n='))
    for i in range(1,n+1):
         L.append(int(input()))
    return x,n,L
def search(L,x):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return None
x,n,L = nhap()
print(search(L,x))