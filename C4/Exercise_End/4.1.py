def nhap():
    while True:
        n = int(input())
        if n > 0:
            return n
def giaithua(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
def inKQ(n,X): 
    print(f'{n}!={X}')
#maincode
n = nhap()
X = giaithua(n)
inKQ(n,X)