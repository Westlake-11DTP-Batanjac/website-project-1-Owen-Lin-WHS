number=int(input('what is your number: '))
check=1
if number%2==0:
    print('not prime')
else:
    while True:
        check+=2
        if check**2>number:
            print('is prime')
            break
        elif number%check==0:
            print('not prime')
            break
