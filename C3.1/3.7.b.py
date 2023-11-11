n=int(input())
for i in range(0,n+1):
    gt=1
    for i in range(1,n+1):
        gt=gt*i
    print(gt)
    n=int(input())