# # Nó bảo câu1 
# # Nhập n 
# # Tính tổng 2 số cuôiis 
# # Vidu n=123
# # Tổng 2+3
# n = (input())
# n_str = str(n)
# if len(n_str) >= 2:
#     sum_2_cuoi = int(n_str[-2]) + int(n_str[-1])
#     print(sum_2_cuoi)
# else:
#     print('end')
n = int(input())
SlC = n%10
SKC = (n//10)%10
print(SKC)
print(SlC+SKC)