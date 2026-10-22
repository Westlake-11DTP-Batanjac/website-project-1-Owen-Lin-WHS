number=int(input('what is your number: '))
for i in range(number):
    if i%15==0:
        print('fizzbuzz')
    elif i%5==0:
        print('buzz')
    elif i%3==0:
        print('fizz')
    else:
        print(i)