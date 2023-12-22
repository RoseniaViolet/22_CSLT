n=int(input('n='))
while n<=100:
    c=0
    i=2
    while i<=n//2:
        if n%i==0:
            c=c+1
            print(n,'khong la SNT')
        i=i+1
        break
    if c==0 and n!=1:
        print(n,'la SNT') 
    break