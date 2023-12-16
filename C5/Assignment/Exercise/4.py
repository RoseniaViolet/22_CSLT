def nhap():
    L=[]
    n = int(input('n='))
    for i in range(1,n+1):
         L.append(int(input()))
    return n,L
def count(L):
    count_result = 0
    for _ in L:
        count_result += 1
    return count_result
n,L = nhap()
print(count(L))