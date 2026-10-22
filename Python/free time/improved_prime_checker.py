num_start=int(input('Choose your number: '))
list=[3]
print(2)
for num in range(3, num_start, 2):
    i=-1
    while True:
        i+=1
        if list[i]**2>num:
            print(num)
            list.append(num)
            break
        elif num%list[i]==0:
            break