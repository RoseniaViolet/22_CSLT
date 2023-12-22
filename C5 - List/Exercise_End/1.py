def Input():
    L = []
    n = int(input('n='))
    if n > 0 :
        for i in range(1, n+1):
            L.append(int(input()))
        x = int(input('x='))
        return L, x, n
    else:
        return None
def FirstAndLast(L):
    result = [L[0], L[-1]]
    print(result)
    return result
def Search(L, x):
    for i in range(len(L)):
        if x == L[i]:
            return True
    return False 

input_result = Input()
if input_result is not None:
    L, x, n = input_result
    result_list = FirstAndLast(L)
    print(Search(result_list, x))
else:
    print("Không có giá trị hợp lệ từ hàm Input.")

