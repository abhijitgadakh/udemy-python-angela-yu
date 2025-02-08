your_name = input("Enter your name: ")
their_name = input("Enter their name: ")

combined_name = (your_name + their_name).lower()

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

first_digit = t + r + u + e

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')

second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if(score < 10 or score > 90):
    print(f'Your Score is: {score}, you go like coke and mentos.')
elif(score >= 40 and score <= 50):
    print(f'Your Score is: {score}, you are great together.')
else:
    print(f'Your Score is: {score}')