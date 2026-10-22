count=int(input('The length of the ribbon: '))
values=input('type the values(a b): ')+' '
current=0
system=''
split=0
length=0
maxlen=0
print(len(values))
for n in range(len(values)):
    if values[n]==' ':
        symbol=int(system)
        if current+1!=symbol:
            split+=1
            if length>maxlen:
                maxlen=length
                length=0
        else:
            length+=1
        current=symbol
        system=''
    else:
        system=system+values[n]
print(split, maxlen)