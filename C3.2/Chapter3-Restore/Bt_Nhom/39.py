D= int(input('Enter a number of decibels:'))
if D == 130:
    print('Jackhammer')
elif D == 106:
    print('Gaslawnmower')
elif D == 70:
    print('Alarm clock')
elif D == 40:
    print('Quiet room')
elif 40<D<70 or 70<D<106 or 106<D<130:
    print('The noise level is between')
elif D < 40:
    print('The noise level is too low to be heard')
else:
    print('The noise level is too loud to be heard')