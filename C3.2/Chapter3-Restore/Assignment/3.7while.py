while True:
    n=int(input())
    s=1
    i=1
    if n>=0:
        while i<=n:
            s=s*i
            i=i+1
        print(s)
    else:
        break