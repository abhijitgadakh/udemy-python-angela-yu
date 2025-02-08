print('Thank you for choosing Python Pizza.')
bill = 0

size = input('What size of pizza you want? S, M, L: ').lower() # S15, M20, L25

if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25
else:
    print("Invalid size selected!")
    exit()


add_pepperoni = input('Do you want Pepperoni: Y or N: ').lower() #Extra S-> 2 | M/L->3

if add_pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3
    print('Pepperoni added.')

elif add_pepperoni == 'n':
    print('Okay. Pepperoni not added.')

else:
    print("Invalid size selected!")
    exit()

extra_cheese = input('Do you want Extra Cheese: Y or N: ').lower() #Extra 1


if extra_cheese == 'y':
    bill += 1
    print('Extra cheese added.')

elif extra_cheese == 'n':
    print('Okay. Extra cheese not added.')

else:
    print("Invalid size selected!")
    exit()


print(f'Your Total Bill is: ${bill}')