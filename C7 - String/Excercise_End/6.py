x=input()
a=x.split(',')
b=[]
for i in range(0,len(a)):
    if int(a[i],2)%3==0:
        b=b+[a[i]]
print(','.join(b))
        
