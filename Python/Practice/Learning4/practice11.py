word=input('give me a word:')
letter=input('give me a letter:')
value=''
for i in range(len(word)):
    if word[i]==letter:
        value+=letter
    else:
        value+=' '
print(value)