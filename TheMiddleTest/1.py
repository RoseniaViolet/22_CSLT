a = int(input())
b = int(input())
result = 0
if a <= b and a>0 and b>0 :
    for i in range(a,b):
        result += i
print(result)