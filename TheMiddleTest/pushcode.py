def add(L, x, k):
    if k > len(L):
        L.append(x)
    else:
        L.insert(k, x)
    return L

# Lệnh nhập
L = list(map(int, input().split()))
x, k = map(int, input().split())
add_result = add(L, x, k)
print(add_result)
def search(L, x):
    for i, value in enumerate(L):
        if value == x:
            return i
    return None

# Lệnh nhập
L = list(map(int, input().split()))
x = int(input())
search_result = search(L, x)
print(search_result)
def delete(L, x):
    L = [item for item in L if item != x]
    return L

# Lệnh nhập
L = list(map(int, input().split()))
x = int(input())
delete_result = delete(L, x)
print(delete_result)
def count(L):
    return len(L)

# Lệnh nhập
L = list(map(int, input().split()))
count_result = count(L)
print(count_result)
def replace(L, x, y):
    for i in range(len(L)):
        if L[i] == x:
            L[i] = y
    return L

# Lệnh nhập
L = list(map(int, input().split()))
x, y = map(int, input().split())
replace_result = replace(L, x, y)
print(replace_result)
