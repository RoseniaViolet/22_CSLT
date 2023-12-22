L = []
n = int(input('n='))
if n > 0 :
    for _ in range(1, n+1):
        L.append(int(input()))
    M = []
    for j in L:
        if j not in M:
            M.append(j)
    for x in M:
         print(x,end=' ')