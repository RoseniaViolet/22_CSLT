n=int(input())
while n>=0:
    i=1
    gt=1
    while i<=n:
        gt=gt*(n-(i-1))
        i=i+1
    print(gt)
    n=int(input())