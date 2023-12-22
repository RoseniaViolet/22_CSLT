L=[]
x = int(input())
y = int(input())
n = int(input())
for i in range(1,n+1):
    L.append(int(input()))
def Replace(L, x, y):
    for i in range(len(L)):
        if L.pop(L[i]) == x:
            L[i] = y
    return L
print(Replace(L,x,y))

