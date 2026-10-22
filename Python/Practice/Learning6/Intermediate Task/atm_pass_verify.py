pin='1234'
guesses=3
while True:
    pin_guess=input('what is the pin: ')
    if pin_guess==pin:
        print('success')
        break
    else:
        guesses-=1
    if guesses==0:
        print('locked out')
        break