text = """
--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.
"""
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = lines[i].replace('-', ' ')
    lines[i] = lines[i].split()
    lines[i] = ' '.join(lines[i])
print(lines)
text = '\n'.join(lines)
print(text)

# # join(ListOfString): ListOfString là một List gồm các chuỗi ký tự. join() dùng để
# nối các phần tử trong ListOfString bằng một chuỗi tương ứng của phương thức
# split(str): dùng để tách mỗi từ nằm trong chuỗi tương ứng thành một list, mỗi
# phần tử nằm trong list là một chuỗi con