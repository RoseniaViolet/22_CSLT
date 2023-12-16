def nhap():
    L=[]
    x = int(input('x='))
    k = int(input('k='))
    n = int(input('n='))
    for i in range(1,n+1):
         L.append(int(input()))
    return x,n,k,L
def add(k,L,x):
    if k > len(L):
        L.append(x)
    else:
        L.insert(k, x)
    return L
x,n,k,L = nhap()
print(add(k,L,x))