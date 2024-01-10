def nhap():
    while True:
        try:
            s = str(input())
            a = int(input())
            b = int(input())
        except:
            print('Dinh dang dau vao khong hop le!')
        else:
            if a > 0 and b > 0:
                if a <= b:
                    if  b <= len(s):
                        return a,b,s
                    else:
                        print('a, b lon hon do dai cua chuoi!')
                else:
                    print('Vui long nhap a<=b')
            else:
                print('Vui long nhap a,b la so tu nhien')
def XuLyChuoi(s):
    reverse = s[::-1]
    return reverse
def Inkq(a,b,s):
    print(s[a:b+1:1])
a,b,s = nhap()
reverse = XuLyChuoi(s)
Inkq(a,b,reverse)
    

