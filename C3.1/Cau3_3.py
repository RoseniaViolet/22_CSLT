TieuThu=int(input('Tieu thu='))
VAT= 0.1
if 1<=TieuThu<=100: 
    ThanhTien= TieuThu*550*1.1
if 101<=TieuThu<=150: 
    ThanhTien= (100*550 + (TieuThu-100)*750)*1.1
if 151<=TieuThu<=200: 
    ThanhTien= (100*550 + 50*750 + (TieuThu-150)*950)*1.1
if TieuThu>=201: 
    ThanhTien= (100*50 + 50*750 + 50*950 + (TieuThu-200)*1350)*1.1
print('Phai tra=', ThanhTien, sep='')