a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
S=(a+b+c)/2
import math
print('Dien tich=' + str(float(math.sqrt(S*(S-a)*(S-b)*(S-c)))))