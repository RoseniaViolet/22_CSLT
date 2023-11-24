s=0
n=int(input('n='))
for i in range(1,n+1):
        print('So thu',i,':',sep="",end="")
        x=int(input())
        if x<0:
            continue
        elif x==0:
            break
        else:
            s=s+x
print('S=',s,sep="")