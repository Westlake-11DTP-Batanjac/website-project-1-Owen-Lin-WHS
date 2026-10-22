import random
while True:
    ai=random.randint(1,3)
    if ai==1:
        ai='scissors'
    elif ai==2:
        ai='rock'
    else:
        ai='paper'
    you=input('your choice: ')
    if you=='exit':
        break
    elif ai==you:
        print('draw')
    elif (you=='paper' and ai=='rock') or (you== 'scissors' and ai=='paper') or (you=='rock' and ai=='scissors'):
        print('win')
    elif (ai=='paper' and you=='rock') or (ai== 'scissors' and you=='paper') or (ai=='rock' and you=='scissors'):
        print('lose')