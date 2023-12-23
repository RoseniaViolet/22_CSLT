A = str(input())
B = A.split(',')
C = []
for i in B:
    if i not in C:
        C.append(i)
C.sort()
E = ','.join(C)
print(E)
            
