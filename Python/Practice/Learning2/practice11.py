score=int(input('What is your test score (in percent without %):'))
if score>100:
    print('invalid')
elif score>80:
    print('A')
elif score>60:
    print('B')
elif score>40:
    print('C')
elif score>20:
    print('D')
else:
    print('E')