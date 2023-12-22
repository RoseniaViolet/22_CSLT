# Kytu = input()
# n = int(input())
# while True:
#      if 1 <= n <= 20:
#          for i in range(n + 1):
#              for j in range(i):
#                  print(Kytu, end=' ')
#              print()
#      break
Kytu = input()
n = int(input())

if 1 <= n <= 20:
    for i in range(n + 1):
        for j in range(i):
            print(Kytu, end=' ')
        print()

