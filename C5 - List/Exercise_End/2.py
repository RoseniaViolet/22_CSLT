def Input():
    L = []
    n = int(input('n='))
    if n > 0:
        for i in range(1, n + 1):
            L.append(int(input()))
        return L, n
    else:
        return None

def Search(L):
    L.sort()
    return L

def Output(min, max):
    print(max, min)

result = Input()
if result is not None:
    L, n = result
    L = Search(L)
    min, max = L[0], L[-1]
    Output(min, max)