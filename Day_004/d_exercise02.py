import random

# Aarav, Priya, Arjun, Sneha, Rahul
friends = input("Enter friends name (Comma seperated): ").split(", ")

person_to_pay = random.randint(0, len(friends)-1)

print(f'This Time "{friends[person_to_pay]}" will pay the bill...!')

