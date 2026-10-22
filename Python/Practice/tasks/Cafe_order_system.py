Menu_items=["Coffee","Tea","Muffin","Sandwich"]
prices=[3.5, 2.5, 4.0, 6.0]
Receipt=[]

print('Welcome to Code Cafe!')
Name=input("What is your name: ")
print("Here is our menu:")

for i in range(len(Menu_items)):
    print(str(i+1)+'.', Menu_items[i],'-','$'+str(prices[i]))

while True:
    Order=input("What would you like to order: ")
    if Order.lower() in (item.lower() for item in Menu_items):
        for n in range(len(Menu_items)):
            if Menu_items[n].lower()==Order.lower():
                Receipt.append(n)
                print(Receipt)
                break
        if input('Would you like to order another item: ').lower()=='no':
            break
    elif int(Order)>=1 and int(Order)<5:
        Receipt.append(int(Order)-1)
cost=0
print('--- Receipt for', Name, '---')
for i in range(len(Receipt)):
    print(Menu_items[Receipt[i]],'- $'+str(prices[Receipt[i]]))
    cost+=prices[Receipt[i]]
print('Total: $'+str(cost))
print('Thank you for ordering at Code Cafe!')