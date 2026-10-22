import random
answers=[
    'Yes',
    'No',
    'of course',
    'Impossible',
    'Go right', 
    'Go left',
    'What do you mean. FAILIURE',
    'you dumb boy',
    'Alt + F4',
    'Are you a chungus? Because you\'re asking a dumb question',
    'the stars aligned for once',
    'history says that you are an interesting person but not today'
    ]

while True:
    type=input("What is your question: ")
    if type=='':
        continue
    elif type=='exit':
        break
    try:
        type=int(type)
    except:
        number=random.randint(0,len(answers)-1)
        print(answers[number])
    else:
        print(type)
    
