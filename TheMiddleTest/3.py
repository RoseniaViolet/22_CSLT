w = int(input())
h = int(input())
CMT = 'ABCDE'
NhapMT = input()
MT = 0
KDG = 'yn'
NhapKDG= input()
if w <= 1000 and h < 30000:
    if NhapMT in CMT:
         if NhapMT == 'A':
            MT = 0
         if NhapMT == 'B':
            MT = 0.1
         if NhapMT == 'C':
            MT = 0.2
         if NhapMT == 'D':
            MT = 0.29
         if NhapMT == 'E':
            MT = 0.35
    if NhapKDG in KDG:
         if NhapKDG == 'y':
             TDG = 10
         else:
             TDG = 0
    Thue = w*h*MT
    Tienluongtuan = w*h+Thue+TDG
    print(f'{Tienluongtuan:.1f}')
        