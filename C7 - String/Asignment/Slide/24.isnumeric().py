while True:
    a = (input())
    b = (input())
    if  a.isdecimal() and b.isdecimal():
        tong = int(a)+int(b)            
        print(tong)
        break
    else:
        print('Please enter a number for your age.')