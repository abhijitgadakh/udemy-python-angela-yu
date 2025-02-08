line1 = ["", "", ""]
line2 = ["", "", ""]
line3 = ["", "", ""]

map = [line1,  line2, line3]

abc = ['a', 'b', 'c']

location = input('Enter Location: ')


column = abc.index(location[0].lower())
number = int(location[1])

map[number-1][column] = "x"

print(f'{line1}\n{line2}\n{line3}')
