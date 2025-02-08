student_heights = input("Enter heights of all student ( comma separated): ").split(", ")

total_height = 0

for height in student_heights:
    total_height += int(height.strip())
    
print(f'Average height of students is : {total_height / len(student_heights)}')
