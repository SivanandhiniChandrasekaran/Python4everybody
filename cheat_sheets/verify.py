# Guess The Number
import random

def guess(x):

    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 to {x}: '))
        if guess < random_number:
            print('Sorry, guess again, Too low.')
        elif guess > random_number:
            print('Sorry, guess again, Too high.')

    print(f'YAY! You guessed the number {random_number} correctly.')



from datetime import datetime

date_time_str = '18/09/19 01:55:19'

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')


print("The type of the date is now",  type(date_time_obj))
print("The date is", date_time_obj)

