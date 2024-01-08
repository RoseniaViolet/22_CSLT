def Input():
    L = []
    n = int(input())
    while True:
        if n > 0:
            for _ in range(n):
                n = int(input())
                L.append(n)
            x = int(input('x='))
            return L,x
        else:
            print('Khong hop le')
def FirstAndLast(L):
    L = [L[0],L[-1]]
    print(L)
def Search(L,x):
    for i in range(len(L)):
        if L[i] == x:
            return True
    return False
#main code
L,x = Input()
FirstAndLast(L)
print(Search(L,x))