print('Welcome to rollercoaster!')

height = int(input("Enter you height in cm: "))

if height >= 120:
    print('You can ride the rollercoaster')
    age = int(input("Enter you age in years: "))

    if age <= 12:
        print('Child tickets are $5.')
    elif age <= 18:
        print('Youth tickets are $7.')
    else:
        print('Adult tickets are $12.')

else:
    print('Sorry, You have to grow taller before you can ride the rollercoaster')