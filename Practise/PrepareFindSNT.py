
n = int(input("Nhập n: "))

# Tìm số nguyên tố lớn nhất bé hơn n
max_prime = -1
i = 2
while i < n:
  # Kiểm tra số nguyên tố
  is_prime = True
  j = 2
  while j * j <= i:
    if i % j == 0:
      is_prime = False
      break
    j += 1
  # Cập nhật số nguyên tố lớn nhất
  if is_prime and i > max_prime:
    max_prime = i
  i += 1

# In kết quả
if max_prime == -1:
  print("Không có số nguyên tố nào bé hơn", n)
else:
  print("Số nguyên tố lớn nhất bé hơn", n, "là", max_prime)

            