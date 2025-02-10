import random
from hangman_words import word_list
from hangman_display import stages, logo

random_word = random.choice(word_list)
display = []
for _ in random_word:
    display += "_"

print(logo)
print(random_word)
print(display)


attempts = 6
print(stages[attempts])
while attempts > 0:

    letter = input("Guess a letter: ").lower()
    is_guess = False
    
    if(letter in display):
        print(f"You have already guessed {letter}")
        break

    for position in range(len(random_word)):
        
        
        if random_word[position] == letter:
            display[position] = letter
            is_guess = True

    if is_guess:
        print("Yaay Right Guess!")
        print(" ".join(display))
    else:
        attempts -= 1
        print(f"Wrong Guess! {attempts} remaining")
        print(stages[attempts])
        
    if not "_" in display:
        print("Congratulations You WON...!")
        break
        
if attempts == 0:
    print("OH NO You Lost...!")
