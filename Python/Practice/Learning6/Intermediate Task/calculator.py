while True:
    operation=input('type your operation:')
    if operation=='exit':
        break
    num1=int(input('type your number:'))
    num2=int(input('type your number:'))

    if operation=='+':
        print(num1+num2)
    elif operation=='-':
        print(num1-num2)
    elif operation=='*':
        print(num1*num2)
    elif operation=='/':
        print(num1/num2)
    