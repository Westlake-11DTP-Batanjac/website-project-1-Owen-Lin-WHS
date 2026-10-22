# the location where you store the questions in sequencial order without any conflicts
# minimum questions is 5
Questions=[
    {
        "type":"Number",
        "Question":"When was the first Lord of the Ring movie released?",
        "Correct Answer":2001
    },

    {
        "type":"Multichoice",
        "Question":"Which country was Lord of the Rings filmed?",
        "A":"United States of America",
        "B":"New Zealand",
        "C":"United Kingdom",
        "D":"Australia",
        "Correct Answer":"b"
    },

    {   
        "type":"Open",
        "Question":"Who was the Director for the Lord of the Rings?",
        # all possible correct answer variation please (lowercase)
        "Correct Answer":["peter jackson","peter","jackson"]
    },

    {
        "type":"Boolean",
        "Question":"True or false? Lord of the Rings has earned more than 1 Billion Dollars worldwide.",
        "Correct Answer":"True"
    },

    {
        "type":"Number",
        "Question":"How many awards did Lord of the Rings get?",
        "Correct Answer":475
    },

    {
        "type":"Multichoice",
        "Question":"What is the name of the movie in Lord of the Rings?",
        "A":"Lord of the Rings: The Fate of the ring",
        "B":"Lord of the Rings: The Trip of the ring",
        "C":"Lord of the Rings: The Sdventure for the ring",
        "D":"Lord of the Rings: The Fellowship of the ring",
        "Correct Answer":"d"
    },

    {
        "type":"Number",
        "Question":"How many movies are there for Lord of the Rings?",
        "Correct Answer":3
    },

    {
        "type":"Number",
        "Question":"What was their budget (in million dollars) during Lord of the Rings creation in its year?",
        "Correct Answer":281
    },

    {
        "type":"Boolean",
        "Question":"True or False? Lord of the Ring is based on a vision he saw.",
        "Correct Answer":"false"
    }

    # if required can be used as a template to help add new questions
    #    {
    #        # only 4 possible choices
    #        "type":"Multichoice",
    #        "Question":"",
    #        "A":"",
    #        "B":"",
    #        "C":"",
    #        "D":"",
    #        "Correct Answer":"a"
    #    },

    #    {   
    #        # 3 word answer at most please
    #        "type":"Open",
    #        "Question":"",
    #        # all possible correct answer variation please
    #        "Correct Answer":["hello"]
    #    },

    #    {
    #        # type true or false as the answer
    #        "type":"Boolean",
    #        "Question":"",
    #        "Correct Answer":""
    #    },

    #    {
    #        # type a number answer
    #        "type":"Number",
    #        "Question":"",
    #        "Correct Answer":0
    #    }
    ]

possible_multichoice_answer=['a','b','c','d']
possible_boolean_answer=['true','false','t','f']



# The normal introduction of the quiz show
print('Welcome to the Lord of the Rings quiz show!')

# Check the amount of questions there are. Goes through the different questions for the amount chosen.
print('There will be', len(Questions), "questions that you'll have to complete containing open, multichoice, and True and false questions on Lord of the rings.")

score=0

# checks what type of question is it
for Q_no in range(len(Questions)):
    print('Question', Q_no+1,':')   

                            
    # Open question
    if Questions[Q_no]["type"].lower()=="open":
        print(Questions[Q_no]["Question"])

        answer_word=input('Type your answer (no symbols, numbers or typos): ')

        #if the answer is correct from the answers provided
        if answer_word.lower() not in Questions[Q_no]["Correct Answer"]:
            print("Wrong answer. The correct answer was", Questions[Q_no]["Correct Answer"][0].lower(),"\nNo points gained\n")
            
        #if the answer is incorrect
        else:
            print('Correct answer! You gained 1 point\n')
            score+=1

    # True or false question
    elif Questions[Q_no]["type"].lower()=="boolean":
        while True:
            print(Questions[Q_no]["Question"])

            answer_TF=input('Type your answer: ').lower()

            # make possible answers for true and false into just true and false
            if answer_TF=='t':
                answer_TF='true'
            elif answer_TF=='f':
                answer_TF='false'

            # if the answer is invalid
            if answer_TF not in possible_boolean_answer:
                print('invalid input please try again')
                continue
            # if the answer is incorrect
            elif answer_TF!=Questions[Q_no]["Correct Answer"].lower():
                print("Wrong answer. The correct answer was", Questions[Q_no]["Correct Answer"].lower(), "\nNo points gained\n")
                break
            #if the answer is correct
            else:
                print('Correct answer! You gained 1 point\n')
                score+=1
                break
            
    # multichoice question
    elif Questions[Q_no]["type"].lower()=="multichoice":
        while True:
            print(Questions[Q_no]["Question"])
            print('A:',Questions[Q_no]["A"])
            print('B:',Questions[Q_no]["B"])
            print('C:',Questions[Q_no]["C"])
            print('D:',Questions[Q_no]["D"])

            answer_letter=input('Type the letter of the answer: ').lower()
            
            # if the inputed answer is invalid
            if answer_letter not in possible_multichoice_answer:
                print('invalid input please try again')
                continue
            # if the inputed answer is incorrect
            elif answer_letter != Questions[Q_no]["Correct Answer"].lower():
                print("Wrong answer. The correct answer was", Questions[Q_no]["Correct Answer"].lower(),"\nNo points gained\n")
                break
            # if the inputed answer is correct
            else:
                print('Correct answer! You gained 1 point\n')
                score+=1
                break

    # number question        
    elif Questions[Q_no]["type"].lower()=="number":
        while True:
            print(Questions[Q_no]["Question"])

            # checks if the answer is a number (no word-number answer)
            try:
                answer_number=int(input('Type the number of the answer (e.g 1,4,15, etc) : '))
            # if the answer was a word answer (invalid answer)
            except:
                print('invalid input please try again')
                continue
            # if the answer was incorrect
            if answer_number != Questions[Q_no]["Correct Answer"]:
                print("Wrong answer. The correct answer was", Questions[Q_no]["Correct Answer"].lower(), "\nNo points gained\n")
                break
            # if the answer was correct
            else:
                print('Correct answer! You gained 1 point\n')
                score+=1
                break

# final result of your quiz
if len(Questions)/2>score:
    print('You have gotten', score, 'points out of', str(len(Questions))+'. Thus it is a FAIL since it is below 50%')
else:
    print('You have gotten', score, 'points out of', str(len(Questions))+'. Thus it is a PASS since it is above 50%')