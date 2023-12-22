L=[]
x = int(input())
k = int(input())
n = int(input())
for i in range(1,n+1):
    L.append(int(input()))
def add(L,x,k):
    if k > len(L):
        L.append(x)
    else:
        L.insert(k, x)
    return L
print(add(L,x,k))