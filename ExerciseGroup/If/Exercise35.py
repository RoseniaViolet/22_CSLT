human_age = int(input('Input a dog age in human years:'))
if human_age < 0:
    print('The age of the dog must be a positive number')
elif human_age <= 2:
    dog_age = human_age * 10.5
else:
    dog_age= 2*10.5 + 4*(human_age-2)
print('The dog age is',dog_age)