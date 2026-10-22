sent=input('what is your sentence with n ending:')
if sent[-1]=="n":
    print(sent[0:-1])
else:
    print('invalid')