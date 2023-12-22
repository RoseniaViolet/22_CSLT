L=[]
x = int(input())
n = int(input())
for i in range(1,n+1):
    L.append(int(input()))
def search(L,x):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return None
print(search(L,x))