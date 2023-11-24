import random

def user_choice():
    choice = int(input('Human: '))
    while choice not in [0, 1, 2, 3]:
        choice = int(input('Human: '))
    return choice

def computer_choice():
    random_value = random.randint(1, 3)
    print(f'Computer: {random_value}')
    return random_value

def determine_winner(user, computer):
    if user == 0:
        return 
    elif user == computer:
        return 'Draw!'
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        return 'Computer Win!'
    else:
        return 'Human Win!'

def play_game():
    while True:
        user = user_choice()

        if user == 0:
            break 
        
        computer = computer_choice()
        result = determine_winner(user, computer)
        print(result)

play_game()
