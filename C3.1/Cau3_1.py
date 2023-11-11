a= float(input('a='))
b= float(input('b='))
c= float(input('c='))
if a<b: 
    SLN=b
    SBN=a
    if SLN<c:
        SLN=c
    elif c<SBN:
        SBN=c
    print('SLN=', SLN, sep='')
    print('SBN=', SBN, sep='')
elif a>b:
    SLN=a
    SBN=b
    if SLN<c:
        SLN=c
    elif c<SBN:
        SBN=c
    print('SLN=', SLN, sep='')
    print('SBN=', SBN, sep='')