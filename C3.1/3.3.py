x= float(input('x='))
y= float(input('y='))
ch= input('Phep toan:')
if ch == '+' :
    print(x, '+', y, '=', round((x+y),1), sep='')
if ch == '-' :
    print(x, '-', y, '=', round((x-y),1), sep='')
if ch == '*' :
    print(x, '*', y, '=', round((x*y),1), sep='')
if ch == '/' :
    if y==0:
        print('Khong hop le')
    else: 
        print(x, '/', y, '=', round((x/y),1), sep='')
else: 
    print('Khong hop le')