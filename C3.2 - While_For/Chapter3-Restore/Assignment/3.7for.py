while True:
    n=int(input())
    if n>=0:
        s=1
        for i in range(1,n+1):
            s=s*i
        print(s)    
    else:
        break
        
            
            