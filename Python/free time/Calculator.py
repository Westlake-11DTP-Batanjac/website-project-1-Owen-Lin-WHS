numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
no_number=0
decoder=''
specific_value=[]
equation=input('type in your equation (+-*/) : ')+' '
for i in range(len(equation)):
    if equation[i] in numbers:
        decoder=decoder+equation[i]
    else: 
        specific_value.append(int(decoder))
        specific_value.append(equation[i])
        print(specific_value)
        no_number+=1
        decoder=''
specific_value.remove(' ')

new_num=0

equation_separate=[specific_value]
for i in range(no_number-1):
    equation_separate.append([])
print(equation_separate)
for iteration in range(len(equation_separate)):
    try:
        divide_location=specific_value.index('/')
    except:
        pass
    for i in range(len(equation_separate[iteration])):
        if i==divide_location-1:
            equation_separate.append(equation_separate[i][iteration]/equation_separate[i+2][iteration])
        elif i==divide_location or i==divide_location+1:
            pass
        else:
            pass