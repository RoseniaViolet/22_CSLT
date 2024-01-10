M = []
L = str(input())
for j in L:
    if j not in M:
        M.append(j)
for x in M:
    print(x,end='')