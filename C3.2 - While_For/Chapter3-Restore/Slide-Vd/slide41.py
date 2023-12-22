n=int(input('n='))
i=1
p=1
if 0<=n<=100:
    while i<=n:
        p=p*(n-(i-1))
        i=i+1
    print(n,'!=',p,sep='')
