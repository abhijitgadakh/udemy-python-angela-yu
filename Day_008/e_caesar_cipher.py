from z_logo import logo


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        index = alphabets.index(letter)
        new_index = (index + shift) % 26

        cipher_text += alphabets[new_index]

    print(f"Encoded Text is {cipher_text}")

def decrypt(cipher_text, shift):
    text = ""
    for letter in text:
        if letter in alphabets:
            index = alphabets.index(letter)
            new_index = (index - shift) % 26

            text += alphabets[new_index]
        else:
            text += letter        

    print(f"Decoded Text is {text}")

            
def caesar(input_text, shift, option):
    text = ""
    if option == 'decode':
        shift *=-1
    for letter in input_text:
        index = alphabets.index(letter)
            
        new_index = (index + shift)

        text += alphabets[new_index]

    print(f"{option}d Text is {text}")

print(logo)

flag = True
while(flag):
    option = input("Type encode or decode: ")
    text = input("Enetr you Text: ").lower()
    shift = int(input("Enter the Shift Number: ")) % 26

    caesar(text, shift, option)
    again = input("type 'yes' to continue and anything else to exit: ").lower()
    if again != "yes":
        flag = False
    

print("Good Bye")