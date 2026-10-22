num_start=int(input('Choose your number:'))
num_end=int(input('Choose your number:'))
for num in range(num_start, num_end):
    check=1
    if num%2!=0:
        while True:
            check+=2
            if check**2>num:
                print(num)
                break
            elif num%check==0:
                break
            else:
                pass