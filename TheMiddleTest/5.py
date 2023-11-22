n=int(input())
snt=2
for i in range(2,n+1):
    if snt % i != 0:
        print(f'{snt} ',end='')
    snt = snt + i