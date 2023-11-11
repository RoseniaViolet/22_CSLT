n = int(input())
if 2 <= n <= 50:
    for i in range(2, n + 1, 2):
        print(i, end=' ')
else:
    print()   