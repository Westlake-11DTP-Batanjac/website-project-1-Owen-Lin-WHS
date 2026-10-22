def integer(value):
    try:
        int(value)
    except:
        integer(input('Type a number:'))
integer(input('Type a number:'))