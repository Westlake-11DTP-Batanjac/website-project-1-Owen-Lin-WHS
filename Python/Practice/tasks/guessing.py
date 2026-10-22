import random
number=random.randint(1,20)
guess=int(input('What is your guess: '))
while number!=guess:
    if guess<number:
        print('Too small')
    elif guess>number:
        print('Too big')
    guess=int(input('What is your guess: '))

print('You got it :D')