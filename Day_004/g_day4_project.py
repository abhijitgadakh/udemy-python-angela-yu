import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('What do you choose:\n')

icons = [ rock, paper, scissors ]
icons_text = [ "rock", "paper", "scissors" ]

your_choice = int(input('0 for Rock, 1 for Paper, 2 for scissors: '))
computer_choice = random.randint(0, 2)

if your_choice < 0 or your_choice > 2:
    print("Invalid Number")

print('Your choice:')
print(icons_text[your_choice])
print(icons[your_choice])

print('computer choice:')
print(icons_text[computer_choice])
print(icons[computer_choice])

if your_choice == computer_choice:
    print("It's a tie")

elif your_choice == 0:
    if computer_choice == 2:
        print("You win")
    else:
        print("You lose")

elif your_choice == 1:
    if computer_choice == 0:
        print("You win")
    else:
        print("You lose")

elif your_choice == 2:
    if computer_choice == 1:
        print("You win")
    else:
        print("You lose")