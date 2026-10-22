month=input('Give me the month:')

if month=='2':
    year=int(input('What is the year:'))
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print('29')
            else:
                print('28')
        else:
            print('29')
    else:
        print('28')
elif month== 1 or month== 3 or month== 5 or month== 7 or month== 8 or month== 10 or month== 12:
    print('31')
else:
    print('30')