duong=0
am=0
while True:
    num = int(input())
    if num>0:
        duong=duong+1
    elif num<0:
        am=am+1
    else:
        break
print(duong,'so duong')
print(am,'so am')