print("Welcome to tip calculator");
total_bill = float(input("What is your total bill: Rs."));
tip = float(input("how much tip you would like to give (in %): "));
people = int(input("how many people to split the bill: "));

bill_per_person = round(((total_bill + (total_bill * (tip / 100))) / people), 2);

print(f"each person should pay Rs.{bill_per_person}");