n = int(input())
ChangeStr = str(n)
a=''
if 0 <= n <= 9999:
     for i in ChangeStr:
            if i == '0' : a += 'A'
            if i == '1' : a += 'B'
            if i == '2' : a += 'C'
            if i == '3' : a += 'D'
            if i == '4' : a += 'E'
            if i == '5' : a += 'F'
            if i == '6' : a += 'G'
            if i == '7' : a += 'H'
            if i == '8' : a += 'K'
            if i == '9' : a += 'L'
     print(a)