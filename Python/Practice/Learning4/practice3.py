num1=int(input('type your number:'))
num2=int(input('type your number:'))
num3=int(input('type your number:'))
num4=int(input('type your number:'))
num5=int(input('type your number:'))
item=[num1, num2, num3, num4, num5]
max_num=num1
for i in range(5):
    if item[i]>max_num:
        max_num=item[i]
    else:
        pass
print(max_num)