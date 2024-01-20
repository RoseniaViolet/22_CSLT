n=int(input())
a=input().split()
a=list(map(int,a))
a=[a[m:m+n] for m in range(0,len(a),n)]
L=[]
for i in a:
    print(*i)
for c in range(0,n):
    L=L+[a[c][c]]
    L=L+[a[n-c-1][c]]
print(L)
print(min(L))
print(max(L))
