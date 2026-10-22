hero_name= input("Enter the name of the superhero: ")
hero_age=input("Enter the age of the superhero: ")

powers={ 
    1: "Flying", 
    2: "Invisibility", 
    3: "Super Strength", 
    4: "Teleportation", 
    5: "Mind Reading", 
    6: "Time Manipulation",
    7: "Wish Granting",
}

for number, power in powers.items(): 
    print(number, "-", power)

chosen_power=powers[int(input("Choose your power: "))]

weaknesses = { 
    "Flying": "Strong wind", 
    "Invisibility": "Bright light", 
    "Super Strength": "Lower stamina",
    "Teleportation": "Can be anywhere",
    "Mind Reading": "Every single thought at once",
    "Time Manipulation": "Can't reverse your own age",
    "Wish Granting": "Genie"
}
print(weaknesses[chosen_power])
score=50
task=int(input('A villain has stolen a powerful device.\nWhat do you do? \n1 - Chase the villain \n2 - Protect the city \n3 - Ask for help\n'))
if task==1:
    print('How? you\'re slow')
    score+=4
elif task==2:
    print('How does that protect the city from a villian that stole a powerful device?')
    score-=5
elif task==3:
    print('Are you a coward?')
    score-=30

print('final score:', score)
print('YOU FAILURE, DO BETTER YOU CAN\'T END LIKE THIS')
