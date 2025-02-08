# SOLUTION 1

end_number = int(input('Enter Number: '))

even_number_total = 0

for number in range(1, end_number + 1):
    if number % 2 == 0:
        even_number_total += number


print(f"Total: {even_number_total}")


# SOLUTION 2

end_number1 = int(input('Enter Number: '))

even_number_total1 = 0

for number in range(2, end_number + 1, 2):
    even_number_total1 += number


print(f"Total: {even_number_total1}")