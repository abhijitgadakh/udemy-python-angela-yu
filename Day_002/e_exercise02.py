height = input("Enter your Height (in m): ");
weight = input("Enter your Weight (in kg): ");

weight_in_int = int(weight);
height_in_int = float(height);

bmi = weight_in_int / (height_in_int ** 2);

print(int(bmi));