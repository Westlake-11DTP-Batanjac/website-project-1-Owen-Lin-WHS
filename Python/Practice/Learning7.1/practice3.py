def longest_word(sentence):
    word=''
    length_word=''
    sentence=sentence+' '
    
    for i in range(len(sentence)):
        if sentence[i]==' ':
            if len(length_word)<len(word):
                length_word=word
            word=''
        else:
            word=word+sentence[i]
    return length_word

answer=longest_word(input('say the sentence: '))
print(answer)