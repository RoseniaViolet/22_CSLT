A = []
n = int(input('n='))
Tong = 0
for i in range(1, n+1):
    A.append(int(input()))
    if i % 2 == 0:
        Tong += A[i-1]
print(f'Tong={Tong}')