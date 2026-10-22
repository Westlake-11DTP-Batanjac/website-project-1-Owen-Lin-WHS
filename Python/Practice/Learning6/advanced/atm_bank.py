balance=1000
while True:
    action=input('what do you do: ')
    if action=='exit':
        break
    amount=int(input('how much money: '))
    if action=='withdrawl':
        if amount>balance:
            print('withdrawl exceeds bank balance')
        else:
            balance-=amount
    elif action=='deposit':
        balance+=amount
