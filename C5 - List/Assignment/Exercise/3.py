L=[]
x = int(input())
n = int(input())
for i in range(1,n+1):
    L.append(int(input()))
def delete(L,x):
    i = 0
    while i < len(L):
        if L[i] == x:
            del(L[i])
        else:
            i += 1
    return L
print(delete(L,x))