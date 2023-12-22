# n = int(input())
# i = 1
# while i <= n:
#      if i % 5 == 1:
#          print()
#      print(i,end = ' ')
n = int(input('n='))
if n >= 1:
    i=0
    while i <= n:
         if i % 5 == 0:
             print()
         print(i,end =' ')
         i += 1
else:
    print('Vui lòng nhập lại')