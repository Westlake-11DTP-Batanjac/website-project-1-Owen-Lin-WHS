number=0
def this(what):
    if what=='a':
        number+=1
        print(number)
        try:
            this('a')
        except:
            this('a')

number=0
this('a')

number=0
print(number)