a = 0
b = 0

while True:
     n = int(input())
     if n > 0:
         a += 1
     elif n < 0:
         b += 1
     else:
         break

print(f'{a} so duong')
print(f'{b} so am')
