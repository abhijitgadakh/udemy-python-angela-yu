scores = input("Enter scores of all student ( comma separated): ").split(", ")

max_score = 0

for score in scores:
    if int(score.strip()) > max_score:
        max_score = int(score.strip())

print('Hightest score: {max_score}')

