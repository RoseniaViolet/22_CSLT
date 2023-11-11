Par_value = int(input('Enter the denomination of a banknote: $'))
if Par_value == 1:
    print('George Washington')
elif Par_value == 2:
    print('Thomas Jefferson')
elif Par_value == 5:
    print('Abraham Lincoln')
elif Par_value == 10:
    print('Alexander Hamilton')
elif Par_value == 20:
    print('Andrew Jackson')
elif Par_value == 50:
    print('Ulysses S. Grant')
elif Par_value == 100:
    print('Benjamin Franklin')
else:
    print('Error! Invalid denomination.')