A=[]
B=[]
for _ in range(10):
    A.append(int(input()))
for i in range(0, len(A)-1, 2):
    B.append(A[i+1])
    B.append(A[i])
for x in B:
    print(x,end=' ')
