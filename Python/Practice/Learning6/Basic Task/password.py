password='something'
while True:
    password_guess=input('what is the password: ')
    if password_guess==password:
        break
print('success')