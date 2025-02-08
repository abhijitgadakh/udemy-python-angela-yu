print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island. Your Mission is to find the Treasure.")

decision = input('\nYou\'re at a cross road. Where do you want to go? Type "left" or "right": ').lower()

if decision == 'left':
    decision = input('\nYou\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
    if decision == 'wait':
        decision = input('\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?: ').lower()
        if(decision == "yellow"):
            print("🎉 You found the treasure! YOU WINNNN!!!!!!!!")
        elif(decision == "red"):
            print("🔥 It's a room full of fire. Game Over.")
        elif decision == "blue":
            print("💀 You enter a room of beasts. Game Over.")
        else:
            print("🚪 That door doesn't exist. Game Over.")
            exit()
    
    elif decision == 'swim':
        print("😱 You got attacked by a giant trout. Game Over.")

    else:
        print("❌ Invalid option selected. Game Over.")
        exit()

elif decision == 'right':
    print("💀 You fell into a hole. Game Over.")

else:
    print("❌ Invalid option selected. Game Over.")
    exit()