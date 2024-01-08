text = """--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình."""
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = lines[i].split('-') 
    while '' in lines[i]:
        lines[i].remove('')
    lines[i] = ' '.join(lines[i])
    print(lines[i])
