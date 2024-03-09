def nhap():
    L = input().split()
    L = list(map(int,L))
    return L

def dem(L):
    for j in L:
        if L.count(j) >= 2:
            return L.count(j)
    return 0

L = nhap()
print(dem(L))