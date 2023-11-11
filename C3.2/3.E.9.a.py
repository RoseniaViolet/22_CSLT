i=1
n = int(input())
while True:
     if 1 >= n or n > 50:
         break
     if 2 <= n <= 50:
         while i <= n:
             if i % 2 == 0:
                 print(i,end=' ')
             i += 1
                 
         