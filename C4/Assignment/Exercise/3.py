def Nhap_2sothuc(a, b):
    a = float(a)
    b = float(b)
    return a, b

def Nhap_Kytu(Kytu):
    if Kytu in ['+', '-', '*', '/']:
        return Kytu
    return None

def Tinh_toan():
    result = None
    a, b = Nhap_2sothuc(input('a='), input('b='))
    operator = Nhap_Kytu(input('Toan_tu:'))
    
    if operator is None:
        print('Ký tự không hợp lệ')
        return None
    
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        try:
            result = a / b
        except ZeroDivisionError:
            print('Error: Chia cho 0')
            return None  
    return f'{a}{operator}{b}={result}'

def Loop():
    while True:
        check = Tinh_toan()
        if check is not None:
            print(check)
        Continue = input('Tiếp tục:')
        if Continue.upper() != 'T':
            break

Loop()

    