num1=int(input('type your number:'))
num2=int(input('type your number:'))
num3=int(input('type your number:'))
num4=int(input('type your number:'))
num5=int(input('type your number:'))
num6=int(input('type your number:'))
num7=int(input('type your number:'))
item=[num1, num2, num3, num4, num5, num6, num7]
sum=0
for i in range(len(item)):
    if item[i]>0:
        sum+=item[i]
    else:
        pass
print(sum)