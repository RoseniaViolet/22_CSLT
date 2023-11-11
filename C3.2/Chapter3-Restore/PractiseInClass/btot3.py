n=int(input('n='))
so=n
dem=0
while n>0:
    d=n%10
    n=int(n/10)
    dem=dem+1
    if n==0:
        break
print(so,'co', dem,'chu so')
    