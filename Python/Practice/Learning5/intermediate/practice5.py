word=input('give me a word:')
letter=input('give me a letter:')
amount=0
for i in range(len(word)):
    if word[i]==letter:
        amount+=1
    else:
        pass
print(amount)