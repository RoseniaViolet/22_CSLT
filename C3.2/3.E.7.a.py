while True:
     n = int(input())
     if n == 0 :
         result = 1
     if n > 0 :
         result = 1
         i = 1
         while i <= n:
             result *= i 
             i += 1     
     if n < 0:
         break
     print(f'{result}')
