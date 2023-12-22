items = []
for i in range(4):
    name = str(input())
    quantity = input()
    items.append((name,quantity))
for name,quantity in items:
    print(f'{name.ljust(20,".")}{quantity.rjust(6," ")}')
    
    
    
    
# Trả về một chuỗi mới khi thêm vào chuỗi gốc các ký tựch, sao cho chiều dài của
# chuỗi đúng bằng n ký tự và chuỗi gốc được đặt nằm bên phải (rjust()), bên trái
# (ljust()) hoặc ở giữa(center()