decibels = int(input('Enter the decibels: '))
if decibels == 130:
    print('Jackhammer')
elif decibels == 106:
    print('Gas lawnmower')
elif decibels == 70:
    print('Alarm clock')
elif decibels == 40:
    print('Quiet room')
elif 40 < decibels < 70:
    print('Between 40 and 70')
elif 70 < decibels < 106:
    print('Between 70 and 106')
elif 106 < decibels < 130:
    print('Between 106 and 130')
elif decibels < 40:
    print('Too low to audible')
else:
    print('Too high to audible')
