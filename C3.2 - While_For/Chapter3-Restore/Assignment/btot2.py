n=int(input('n='))
snt=1
for i in range(2,n,1):
    if (n%i==0):
        snt=0
        break
if snt==1:
    print(n,'la SNT')
else:
    print(n,'khong la SNT')