print('Welcome to rollercoaster!')

height = int(input("Enter your height in cm: "))
ticket_price = 0

if height >= 120:
    print('You can ride the rollercoaster')
    age = int(input("Enter your age in years: "))

    if age < 12:
        ticket_price += 5
        print(f'Child tickets are ${ticket_price}.')
    elif age <= 18:
        ticket_price += 7
        print(f'Youth tickets are ${ticket_price}.')
    else:
        ticket_price += 12
        print(f'Adult tickets are ${ticket_price}.')

    want_photo = input("Do you want a photo taken? Y or N: ").lower()

    if want_photo == 'y':
        ticket_price += 3

    print(f"Your Final Bill is: {ticket_price}")

else:
    print('Sorry, You have to grow taller before you can ride the rollercoaster')