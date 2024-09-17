import random

random_number: int = random.randint(0,20)

number_of_guesses = (1,2,3,4,5)

for count in number_of_guesses:
    guess = int(input('Enter the number'))
    if guess == random_number:
        print('ACCESS GRANTED')
        break

    elif guess < random_number:
        print('To low. try again!')
        print('Try count:', count)

    elif guess > random_number:
        print('To high. try again!')
        print('Try count:', count)

    elif number_of_guesses == 5:
        break

if count == 5 and guess != random_number:
    print('SYSTEM LOCKED')


#funktioner rep
#callstack - 