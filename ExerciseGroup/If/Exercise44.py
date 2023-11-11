month = input('Enter the month: ')
day = int(input('Enter the day: '))

if month == "January" and day == 1:
    print("New Year's Day")
elif month == 'July' and day == 1:
    print('Canada Day')
elif month == 'December' and day == 25:
    print('Christmas Day')
else:
    print('No fixed holiday for the entered month and day.')