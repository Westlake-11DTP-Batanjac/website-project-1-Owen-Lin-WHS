shopping_list = {
    'banana':3.50,
    'carrots':2.00,
    'steak':24.50,
    'ice cream':5.99,}
def add(thing, value):
    shopping_list[thing]=value

add(input('thing: '),int(input('value: ')))
number=0
for value in shopping_list.values():

    number+=int(value)
print(number)