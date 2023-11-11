n=int(input())
mahoa=['A','B','C','D','E','F','G','H','K','L']
for i in range(len(str(n))-1,-1,-1):
    a=int(n/10**i)
    n=n%10**i
    print(mahoa[a],end='')