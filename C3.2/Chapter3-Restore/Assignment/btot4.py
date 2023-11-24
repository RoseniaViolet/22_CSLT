while True:
    a=float(input('a='))
    b=float(input('b='))
    ttu=input('Toan tu:')
    if ttu=='+':
        print(f'{a}{ttu}{b}={a+b}')
    elif ttu=='-':
        print(f'{a}{ttu}{b}={a-b}')
    elif ttu=='*':
        print(f'{a}{ttu}{b}={a*b}')
    elif ttu=='/':
        print(f'{a}{ttu}{b}={a/b}')
        tt=input('Tiep tuc:')
        if tt=='T' or tt=='t':
            break