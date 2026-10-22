birth_date=int(input('what is the birth date:'))
birth_month=int(input('what is the birth month:'))
birth_year=int(input('what is the birth year:'))
target_date=int(input('what is the target date:'))
target_month=int(input('what is the target month:'))
target_year=int(input('what is the target year:'))
if target_year-birth_year<16:
    print('inelegible')
elif target_month>birth_month:
    print('inelegible')
elif target_date<birth_date:
    print('inelegible')
else:
    print('elegible')
