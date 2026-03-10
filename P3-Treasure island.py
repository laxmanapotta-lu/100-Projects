# It is simple code of Tresure island

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("Level-1")
print("This game completely depend on choices you enter ")

print("1.Right")
print("2.Left")
choice = int(input(" Enter the Choice : "))
if choice==1:
    print(" Game over ")
elif choice == 2:
    print(" You are now go to the next level ")
    
    print("Level-2")
    print("Now once more you select the given choices ")
    print("1.Swim")
    print("2.Wait")
    choice=int(input(" Enter the choice: "))
    if choice ==1:
        print(" Crocodile will bite you ! Game over ")
    elif choice ==2:
        print(" You are now go to the next level ")

        print(" Level-3")
        print(" Now once more you select the given choices ")
        print("There are three diffrent colour doors please select you want to move ")
        print("1.Yellow")
        print("2.Red")
        print("3.Green")
        choice=int(input(" Enter the Colour of the door no: "))
        if choice==1:
            print(" It is full of snakes , it bite you , Game Over!")
        elif choice ==2:
            print(" It is full of fire , then  Game over ")
        elif choice == 3:
            print(" You win ! You will find the treasure box ")

else:
    print(" Invalid choice ! Please enter valid choice ")

