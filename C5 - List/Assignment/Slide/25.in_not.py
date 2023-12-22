L = []
St = input()
while St != '':
    if St not in L:
        L += [St]
    St = input()
print(L) 