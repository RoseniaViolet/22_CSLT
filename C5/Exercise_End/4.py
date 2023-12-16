A = []
n = int(input('n='))
for i in range(1, n + 1):
    A.append(int(input()))
B = A[::-1]
print(B)
B.sort()
print(B)