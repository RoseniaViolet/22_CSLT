t=''
while t!='t' and t!='T':
    a=float(input('a='))
    b=float(input('b='))
    toantu=input('Toan tu:')
    if toantu=='+':
        print (a,toantu,b,'=',a+b,sep='')
    elif toantu=='-':
        print (a,toantu,b,'=',a-b,sep='')
    elif toantu=='*':
        print (a,toantu,b,'=',a*b,sep='') 
    elif toantu=='/' and b!=0:  
        print (a,toantu,b,'=',a/b,sep='')
    elif toantu=='/' and b==0:
        print('Khong hop le')
    t=input('Tiep tuc:')