amount=int(input('number:'))
check=1
for i in range(amount):
    while True:
        n=1
        check+=1
        while check%(2**n)==0:
            n+=1
        n-=1
        m=1
        while check%(3**m)==0:
            m+=1
        m-=1
        x=1
        while check%(5**x)==0:
            x+=1
        x-=1
        if ((check/(5**x))/(3**m))/(2**n)==1:
            print(check, i)
            break
print(check)