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
    Max = max(L)
    Min = min(L)
    return Max,Min

def Output(Max,Min):
    print(Max, Min)

result = Input()
if result is not None:
    L, n = result
    Max,Min = Search(L)
    Output(Max,Min)