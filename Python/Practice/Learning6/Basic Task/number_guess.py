import random
secret=random.randint(1,10)

while True:
    guess=int(input('What number are you guessing: '))
    if secret== guess:
        break

print('You got it!')