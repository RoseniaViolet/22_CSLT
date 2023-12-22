st1 = str(input())
st2 = str(input())
st3 = str(input())
index = st1.find(st2)
print(f"Vị trí xuất hiện st2: {index}")
result = st1.replace(st2,st3)
print(f"Xâu kết quả: {result}")




# Tìm và thay thế các chuỗi oldvalue xuất hiệntrong chuỗi gốc bằng newvalue, với
# n lần tìm và thay thế;
# Nếu không có n: thì mặc định là tất cả các lần xuất hiện.