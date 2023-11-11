a = input("Enter month: ")
if a in {'January', 'March', 'May', 'July', 'August', 'October', 'December'}:
    print(a, "has 31 days")
elif a == "February":
    print(a, "has 28 or 29 days")
elif a in {'April', 'June', 'November', 'September'}:
    print(a, 'has 30 days')
else:
    print(f'Invalid month: {a}')

