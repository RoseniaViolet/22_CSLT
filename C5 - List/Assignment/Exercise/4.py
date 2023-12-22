L=[]
n = int(input())
for i in range(1,n+1):
    L.append(int(input()))
def count(L):
    count_result = 0
    for _ in L:
        count_result += 1
    return count_result
print(count(L))